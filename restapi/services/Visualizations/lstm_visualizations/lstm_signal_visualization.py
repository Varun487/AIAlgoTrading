import datetime
import matplotlib.pyplot as plt
import io
import base64

from services.Visualizations.visualization import Visualization

from strategies.models import TickerData

from services.Utils.getters import Getter

from backtester.models import BackTestTrade

from services.IndicatorCalc.indicators import AllIndicators
from services.SignalGeneration.lstmsignalgenerator import LSTMSignalGenerator


class LSTMSignalVisualization(Visualization):
    def __init__(self, backtest_report=None, height=-1, width=-1):
        super().__init__(backtest_report, height, width)

    def generate_visualization(self):
        # Get ticker data in db
        df = Getter(
            table_name=TickerData,
            df_flag=True,
            param_list={
                'company': self.backtest_report.company,
                'time_stamp__range': [
                    self.backtest_report.start_date_time,
                    self.backtest_report.end_date_time
                ]
            }
        ).get_data()

        # Remove df cols
        df.drop(['id', 'company_id', 'time_period'], axis=1, inplace=True)

        # To get signals in df

        # Get all trades corresponding to backtest report
        backtest_trades = list(BackTestTrade.objects.filter(back_test_report=self.backtest_report))

        # Get signals df
        df = LSTMSignalGenerator(
            indicator=AllIndicators(
                df=df,
                time_period=self.backtest_report.strategy_config.indicator_time_period,
                dimension=self.backtest_report.strategy_config.get_dimension_display(),
                sigma=self.backtest_report.strategy_config.sigma,
            ),
            strategy_config=self.backtest_report.strategy_config,
        ).generate_signals()

        # Add signal of each trade to a signals list
        signals = ['FLAT' for i in range(len(df))]

        time_stamps = list(df['time_stamp'])

        for backtest_trade in backtest_trades:
            i = time_stamps.index(backtest_trade.trade.entry_order.signal.ticker_data.time_stamp)
            if backtest_trade.trade.entry_order.signal.type == "1":
                signals[i] = 'BUY'
            else:
                signals[i] = 'SELL'

        # Add signal col to df
        df['SIGNAL'] = signals

        # Create the visualization
        plt.style.use('dark_background')

        # convert timestamps to datetime objects if strings
        if type(df['time_stamp'][0]) == str:
            df['time_stamp'] = list(
                map(lambda dt: datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S+00:00'), df['time_stamp']))

        # create the graph
        fig, ax1 = plt.subplots(figsize=(self.width, self.height))

        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.set_title("Signals generated on company data")

        buy_markers = list(df[df['SIGNAL'] == 'BUY'].index)
        ax1.plot(df['time_stamp'], df['close'], label='Buy signal', marker='^', color='lime',
                 alpha=1, markevery=buy_markers, markersize=15)

        sell_markers = list(df[df['SIGNAL'] == 'SELL'].index)
        ax1.plot(df['time_stamp'], df['close'], label='Sell signal', marker='v', color='r',
                 alpha=1, markevery=sell_markers, markersize=15)

        ax1.plot(df['time_stamp'], df['trend_sma_fast'], label='Simple Moving Average Fast', color='g')
        ax1.plot(df['time_stamp'], df['trend_sma_slow'], label='Simple Moving Average Slow', color='maroon')
        ax1.plot(df['time_stamp'], df['trend_ema_fast'], label='Exponential Moving Average Fast', color='b')
        ax1.plot(df['time_stamp'], df['trend_ema_slow'], label='Exponential Moving Average Slow', color='purple')
        ax1.plot(df['time_stamp'], df['close'], label='Price', color='lightblue')

        ax1.tick_params(axis='y')

        ax2 = ax1.twinx()  # set up the 2nd axis

        ax2.set_ylabel("Volume")
        ax2.bar(df['time_stamp'], df['volume'], width=0.5, alpha=0.15)
        ax2.grid(b=False)

        ax1.legend()
        fig.tight_layout()

        # plt.savefig("/home/app/restapi/services/Visualizations/lstm_visualizations/test_lstm_signal_visualization_image.png", dpi=100)

        pic_io_bytes = io.BytesIO()

        plt.savefig(pic_io_bytes, format='png')
        pic_io_bytes.seek(0)
        pic_hash = base64.b64encode(pic_io_bytes.read())

        return str(pic_hash)[2:-1]
