import datetime
import matplotlib.pyplot as plt
import io
import base64

from services.Visualizations.visualization import Visualization

from backtester.models import BackTestTrade
from strategies.models import TickerData

from services.IndicatorCalc.indicators import BollingerIndicator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.OrderExecution.orderexecution import OrderExecution
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from services.TradeEvaluation.tradeevaluator import TradeEvaluator
from services.Utils.getters import Getter


class BBTradeVisualization(Visualization):
    def __init__(self, backtest_report=None, backtest_trade=None, height=-1, width=-1):
        super().__init__(backtest_report, height, width)

        self.backtest_trade = backtest_trade
        self.valid_backtest_trade = False

    def validate_backtest_trade(self):
        self.valid_backtest_trade = isinstance(self.backtest_trade, BackTestTrade)

    def validate(self):
        super().validate()
        self.validate_backtest_trade()
        self.valid = self.valid and self.valid_backtest_trade

    def generate_visualization(self):

        trade_number = list(BackTestTrade.objects.filter(
            back_test_report=self.backtest_report
        )).index(self.backtest_trade) + 1

        df = Getter(table_name=TickerData, df_flag=True, param_list={'company': self.backtest_report.company,
                                                                     'time_stamp__range': [
                                                                         self.backtest_trade.back_test_report.start_date_time,
                                                                         self.backtest_trade.back_test_report.end_date_time
                                                                     ]}).get_data()

        df.drop(['id', 'company_id', 'time_period'], axis=1, inplace=True)

        df = BBSignalGenerator(
            indicator=BollingerIndicator(
                df=df,
                time_period=self.backtest_report.strategy_config.indicator_time_period,
                dimension=self.backtest_report.strategy_config.get_dimension_display(),
                sigma=self.backtest_report.strategy_config.sigma,
            )
        ).generate_signals()

        # Add take profit and stop loss price
        df = TakeProfitAndStopLossBB(df=df, dimension=self.backtest_report.strategy_config.get_dimension_display(),
                                     factor=self.backtest_report.strategy_config.take_profit_factor).get_calc_df()

        # Execute orders
        df = OrderExecution(df=df, max_holding_period=self.backtest_report.strategy_config.max_holding_period,
                            dimension=self.backtest_report.strategy_config.get_dimension_display()).execute()

        # Evaluate trades
        df = TradeEvaluator(df=df).get_evaluated_df()

        plt.style.use('dark_background')

        trades_df = df.dropna().reset_index()

        if len(trades_df) == 0:
            raise ValueError("No trades to visualize!")

        if not ((type(trade_number) == int) and (trade_number > 0) and (
                trade_number <= len(df.dropna()))):
            raise ValueError(
                f"Trade number specified is incorrect! It should be between 1 and {len(df.dropna())} inclusive.")

        # determine type of trade
        trade_type = trades_df['SIGNAL'][trade_number - 1]

        # determine start and end indexes
        start_index = trade_number - 1 - 10
        end_index = trades_df['order_exit_index'][trade_number - 1] + 10

        if start_index < 0:
            start_index = 0

        if end_index > (len(df) - 1):
            end_index = len(df) - 1

        df = df.iloc[start_index:end_index + 1].reset_index()

        # convert timestamps to datetime objects if strings
        if type(df['time_stamp'][0]) == str:
            df['time_stamp'] = list(
                map(lambda dt: datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S+00:00'), df['time_stamp']))

        # create the graph
        fig, ax1 = plt.subplots(figsize=(self.width, self.height))

        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.set_title(f'Trade Number {trade_number}')

        signal_marker_index = [trades_df['index'][trade_number - 1]]

        signal_label = 'Buy Signal'
        signal_marker = '^'
        signal_color = 'lime'

        if trade_type == "SELL":
            signal_label = 'Sell Signal'
            signal_marker = 'v'
            signal_color = 'red'

        ax1.plot(df['time_stamp'], df['close'], label=signal_label, marker=signal_marker, color=signal_color,
                 alpha=1, markevery=signal_marker_index, markersize=15)

        ax1.plot(df['time_stamp'], df['bb_bbm'], label='Simple moving Average', color='g')
        ax1.plot(df['time_stamp'], df['bb_bbh'], label='', color='r')
        ax1.plot(df['time_stamp'], df['bb_bbl'], label='Bollinger bands', color='r')
        ax1.plot(df['time_stamp'], df['close'], label='Price', color='b')

        # mark order entry and exit
        ax1.axvline(df['time_stamp'][trades_df['order_entry_index'][trade_number - 1]], label="Order entry",
                    color='white')
        ax1.axvline(df['time_stamp'][trades_df['order_exit_index'][trade_number - 1]], label="Order exit",
                    color='orange')
        ax1.tick_params(axis='y')

        ax2 = ax1.twinx()  # set up the 2nd axis

        ax2.set_ylabel("Volume")
        ax2.bar(df['time_stamp'], df['volume'], width=0.5, alpha=0.15)
        ax2.grid(b=False)

        ax1.legend()
        fig.tight_layout()

        # plt.savefig("/home/app/restapi/services/Visualizations/bb_visualizations/test_bb_trade_visualization_image.png", dpi=100)

        pic_io_bytes = io.BytesIO()

        plt.savefig(pic_io_bytes, format='png')
        pic_io_bytes.seek(0)
        pic_hash = base64.b64encode(pic_io_bytes.read())

        return str(pic_hash)[2:-1]
