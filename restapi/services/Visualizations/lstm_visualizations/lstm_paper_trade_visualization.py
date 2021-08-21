import base64
import datetime
import io

import matplotlib.pyplot as plt
from papertrader.models import PaperTrade
from services.SourceData.sourcedata import SourceData
from services.Visualizations.visualization import Visualization
from services.IndicatorCalc.indicators import AllIndicators


class LSTMPaperTradeVisualization(Visualization):
    def __init__(self, backtest_report=None, paper_trade=None, height=-1, width=-1):
        super().__init__(backtest_report, height, width)

        self.paper_trade = paper_trade
        self.valid_paper_trade = False

        self.company = None
        self.start_date = None
        self.end_date = None
        self.strategy_config = None
        self.signal = None

        self.df = None

    def validate_paper_trade(self):
        self.valid_paper_trade = isinstance(self.paper_trade, PaperTrade)

    def validate(self):
        super().validate()
        self.validate_paper_trade()
        self.valid = self.valid and self.valid_paper_trade

    def generate_visualization(self):
        # Set company
        self.company = self.paper_trade.trade.entry_order.signal.ticker_data.company

        # Set strategy config
        self.strategy_config = self.paper_trade.paper_traded_strategy.strategy_config

        # Set signal
        self.signal = self.paper_trade.trade.entry_order.signal

        # Set start date
        self.start_date = self.paper_trade.trade.entry_order.signal.ticker_data.time_stamp - datetime.timedelta(
            days=self.strategy_config.indicator_time_period + 50
        )

        # Set end date
        self.end_date = self.paper_trade.trade.entry_order.ticker_data.time_stamp + datetime.timedelta(
            days=self.strategy_config.max_holding_period + 10
        )

        # Source data
        self.df = SourceData(
            company=self.company,
            start_date=self.start_date,
            end_date=self.end_date,
        ).get_df()

        # Modify df
        self.df.reset_index(inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)

        # Calculate indicators
        self.df = AllIndicators(
            df=self.df,
            time_period=self.strategy_config.indicator_time_period,
            dimension=self.strategy_config.get_dimension_display(),
            sigma=self.strategy_config.sigma,
        ).calc()

        # Adjust dataframe for graphing
        self.df = self.df.iloc[20:]
        self.df.reset_index(inplace=True)
        # print(self.df)

        # create the graph

        # Choose a dark theme
        plt.style.use('dark_background')

        # First axis
        fig, ax1 = plt.subplots(figsize=(self.width, self.height))

        # Set axes labels and title
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.set_title(f'Paper Trade {self.company}')

        # Get Signal index
        signal_marker_index = []

        for i in range(len(self.df)):
            if self.df['time_stamp'][i].date() == self.signal.ticker_data.time_stamp.date():
                signal_marker_index.append(i)

        # Set signal plot attributes
        signal_label = 'Buy Signal'
        signal_marker = '^'
        signal_color = 'lime'

        if self.signal.type == "2":
            signal_label = 'Sell Signal'
            signal_marker = 'v'
            signal_color = 'red'

        # Plot signal
        ax1.plot(self.df['time_stamp'], self.df['close'], label=signal_label, marker=signal_marker, color=signal_color,
                 alpha=1, markevery=signal_marker_index, markersize=15)

        # Plot close price and indicators
        ax1.plot(self.df['time_stamp'], self.df['trend_sma_fast'], label='Simple Moving Average Fast', color='g')
        ax1.plot(self.df['time_stamp'], self.df['trend_sma_slow'], label='Simple Moving Average Slow', color='maroon')
        ax1.plot(self.df['time_stamp'], self.df['trend_ema_fast'], label='Exponential Moving Average Fast', color='b')
        ax1.plot(self.df['time_stamp'], self.df['trend_ema_slow'], label='Exponential Moving Average Slow', color='purple')
        ax1.plot(self.df['time_stamp'], self.df['close'], label='Price', color='lightblue')

        # Get entry order index
        entry_order_index = -1

        for i in range(len(self.df)):
            if self.df['time_stamp'][i].date() == self.paper_trade.trade.entry_order.ticker_data.time_stamp.date():
                entry_order_index = i

        # Plot entry order
        if entry_order_index != -1:
            ax1.axvline(self.df['time_stamp'][entry_order_index], label="Entry Order", color='white')

        # Get exit order index (if it exists)
        exit_order_index = -1

        if self.paper_trade.trade.exit_order is not None:
            for i in range(len(self.df)):
                if self.df['time_stamp'][i].date() == self.paper_trade.trade.exit_order.ticker_data.time_stamp.date():
                    exit_order_index = i

        # Plot exit order (if exists)
        if self.paper_trade.trade.exit_order is not None:
            ax1.axvline(self.df['time_stamp'][exit_order_index], label="Order exit", color='orange')

        ax2 = ax1.twinx()  # set up the 2nd axis

        ax2.set_ylabel("Volume")
        ax2.bar(self.df['time_stamp'], self.df['volume'], width=0.5, alpha=0.15)
        ax2.grid(b=False)

        ax1.legend()
        fig.tight_layout()

        # plt.savefig("/home/app/restapi/services/Visualizations/lstm_visualizations/test_lstm_paper_trade_visualization_image.png", dpi=100)

        pic_io_bytes = io.BytesIO()

        plt.savefig(pic_io_bytes, format='png')
        pic_io_bytes.seek(0)
        pic_hash = base64.b64encode(pic_io_bytes.read())

        return str(pic_hash)[2:-1]
