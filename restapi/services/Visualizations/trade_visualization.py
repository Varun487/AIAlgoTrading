import datetime
import matplotlib.pyplot as plt
from .visualization import Visualization
import io
import base64


class TradeVisualization(Visualization):
    def __init__(self, df=None, columns=None, height=-1, width=-1, trade_number=-1):
        super().__init__(df, columns, height, width)
        self.trade_number = trade_number

    def generate_visualization(self):
        plt.style.use('dark_background')

        trades_df = self.df.dropna().reset_index()

        if len(trades_df) == 0:
            raise ValueError("No trades to visualize!")

        if not ((type(self.trade_number) == int) and (self.trade_number > 0) and (
                self.trade_number <= len(self.df.dropna()))):
            raise ValueError(
                f"Trade number specified is incorrect! It should be between 1 and {len(self.df.dropna())} inclusive.")

        # determine type of trade
        trade_type = trades_df['SIGNAL'][self.trade_number - 1]

        # determine start and end indexes
        start_index = self.trade_number - 1 - 10
        end_index = trades_df['order_exit_index'][self.trade_number - 1] + 10

        if start_index < 0:
            start_index = 0

        if end_index > (len(self.df) - 1):
            end_index = len(self.df) - 1

        self.df = self.df.iloc[start_index:end_index+1].reset_index()

        # convert timestamps to datetime objects if strings
        if type(self.df['time_stamp'][0]) == str:
            self.df['time_stamp'] = list(
                map(lambda dt: datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S+00:00'), self.df['time_stamp']))

        # create the graph
        fig, ax1 = plt.subplots(figsize=(self.width, self.height))

        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price")
        ax1.set_title(f'Trade Number {self.trade_number}')

        signal_marker_index = [trades_df['index'][self.trade_number - 1]]

        signal_label = 'Buy Signal'
        signal_marker = '^'
        signal_color = 'lime'

        if trade_type == "SELL":
            signal_label = 'Sell Signal'
            signal_marker = 'v'
            signal_color = 'red'

        ax1.plot(self.df['time_stamp'], self.df['close'], label=signal_label, marker=signal_marker, color=signal_color,
                 alpha=1, markevery=signal_marker_index, markersize=15)

        ax1.plot(self.df['time_stamp'], self.df['bb_bbm'], label='Simple moving Average', color='g')
        ax1.plot(self.df['time_stamp'], self.df['bb_bbh'], label='', color='r')
        ax1.plot(self.df['time_stamp'], self.df['bb_bbl'], label='Bollinger bands', color='r')
        ax1.plot(self.df['time_stamp'], self.df['close'], label='Price', color='b')

        # mark order entry and exit
        ax1.axvline(self.df['time_stamp'][trades_df['order_entry_index'][self.trade_number - 1]], label="Order entry",
                    color='white')
        ax1.axvline(self.df['time_stamp'][trades_df['order_exit_index'][self.trade_number - 1]], label="Order exit",
                    color='orange')
        ax1.tick_params(axis='y')

        ax2 = ax1.twinx()  # set up the 2nd axis

        ax2.set_ylabel("Volume")
        ax2.bar(self.df['time_stamp'], self.df['volume'], width=0.5, alpha=0.15)
        ax2.grid(b=False)

        ax1.legend()
        fig.tight_layout()

        plt.savefig("/home/app/restapi/services/Visualizations/test_trade_visualization.png", dpi=100)

        pic_io_bytes = io.BytesIO()

        plt.savefig(pic_io_bytes, format='png')
        pic_io_bytes.seek(0)
        pic_hash = base64.b64encode(pic_io_bytes.read())

        return str(pic_hash)[2:-1]
