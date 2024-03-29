import datetime

from django.utils.timezone import make_aware

from papertrader.models import PaperTradedStrategy
from papertrader.models import PaperSignal

from strategies.models import TickerData, Signal

from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from services.SourceData.sourcedata import SourceData
from services.IndicatorCalc.indicators import BollingerIndicator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.SignalGeneration.lstmsignalgenerator import LSTMSignalGenerator
from services.IndicatorCalc.indicators import AllIndicators

all_strategies = {
    "Simple Bollinger Band Strategy": BBSignalGenerator,
    'LSTM Strategy': LSTMSignalGenerator
}
all_indicators = {
    "Simple Bollinger Band Strategy": BollingerIndicator,
    'LSTM Strategy': AllIndicators
}
all_take_profit_stop_loss_methods = {
    "Simple Bollinger Band Strategy": TakeProfitAndStopLossBB,
    'LSTM Strategy': TakeProfitAndStopLossBB
}


class PaperSignalGenerator(object):
    def __init__(self, test_end_date=None, test_today=None):
        self.df = None
        self.df_last_row = None
        self.ticker_data = None
        self.signal = None

        self.company = None
        self.paper_traded_strategy = None
        self.strategy_config = None
        self.indicator = None
        self.signal_generator = None
        self.take_profit_stop_loss_method = None

        self.start_date = None
        self.end_date = test_end_date
        self.today = test_today

    def set_signal_generator(self):
        # Set indicator and signal generator
        self.indicator = all_indicators[self.strategy_config.strategy_type.name]
        self.signal_generator = all_strategies[self.strategy_config.strategy_type.name]

    def set_take_profit_stop_loss_method(self):
        self.take_profit_stop_loss_method = all_take_profit_stop_loss_methods[self.strategy_config.strategy_type.name]

    def set_df(self):
        # Set start date and end date according to indicator time period
        if self.end_date is None:
            self.end_date = datetime.datetime.now()
        
        self.start_date = self.end_date - datetime.timedelta(
            days=self.strategy_config.indicator_time_period + 40)

        # Source data
        self.df = SourceData(company=self.company, start_date=self.start_date, end_date=self.end_date).get_df()

        # Modify df
        self.df.reset_index(inplace=True)
        # self.df.drop(['Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)

    def generate_signal(self):
        self.df = self.signal_generator(
            indicator=self.indicator(
                df=self.df,
                dimension=self.strategy_config.get_dimension_display(),
                time_period=self.strategy_config.indicator_time_period,
                sigma=self.strategy_config.sigma,
            ),
            strategy_config=self.strategy_config,
        ).get_signals()

        if not self.df.empty:
            self.df = TakeProfitAndStopLossBB(
                df=self.df,
                factor=self.strategy_config.take_profit_factor,
                dimension="close"
            ).get_calc_df()

    def push_ticker_data(self):
        # Push TickerData
        ticker_data = TickerData.objects.filter(company=self.company, time_period="1",
                                                time_stamp=make_aware(self.df_last_row['time_stamp']))

        # if ticker data is not available in the DB, create and push it
        if not ticker_data:
            ticker_data = TickerData(
                time_stamp=make_aware(self.df_last_row['time_stamp']),
                open=self.df_last_row['open'],
                high=self.df_last_row['high'],
                low=self.df_last_row['low'],
                close=self.df_last_row['close'],
                volume=self.df_last_row['volume'],
                company=self.company
            )
            ticker_data.save()
            self.ticker_data = ticker_data

        # if ticker data is available in the DB
        else:
            self.ticker_data = ticker_data[0]

    def push_signal(self):
        # Find signal type
        signal_type = "1"
        if self.df_last_row['SIGNAL'] == 'SELL':
            signal_type = "2"

        # If signal is not present in DB, push the signal
        signal = Signal.objects.filter(type=signal_type, ticker_data=self.ticker_data,
                                       strategy_config=self.strategy_config)
        if not signal:
            signal = Signal(
                type=signal_type,
                ticker_data=self.ticker_data,
                strategy_config=self.strategy_config
            )
            signal.save()
            self.signal = signal

        # If signal is present in DB
        else:
            self.signal = signal[0]

    def push_paper_signal(self):
        # Check if dataframe exists
        if not self.df.empty:
            self.df_last_row = self.df.iloc[len(self.df) - 1]

            if self.today is None:
                self.today = datetime.datetime.today()

            # Check if last timestamp in df is today's timestamp
            if self.df_last_row['time_stamp'].date() == self.today.date():

                # Check if signal is not FLAT
                if self.df_last_row['SIGNAL'] != 'FLAT':
                    # Push ticker data
                    self.push_ticker_data()

                    # Push Signal
                    self.push_signal()

                    # Push Paper Traded Signal
                    PaperSignal(
                        signal=self.signal,
                        paper_traded_strategy=self.paper_traded_strategy,
                        executed=False,
                        take_profit=self.df_last_row['take_profit'],
                        stop_loss=self.df_last_row['stop_loss']
                    ).save()

    def run(self):
        # Get all live traded strategies
        live_traded_strategies = list(PaperTradedStrategy.objects.filter(live=True))

        total = len(live_traded_strategies)
        count = 0

        for strategy in live_traded_strategies:
            # Set paper traded strategy
            self.paper_traded_strategy = strategy

            # Set company
            self.company = strategy.company

            # Set configuration
            self.strategy_config = strategy.strategy_config

            # Identify signal generator
            self.set_signal_generator()

            # Identify take profit and stop loss method
            self.set_take_profit_stop_loss_method()

            # Source latest data for company according to strategy config
            self.set_df()

            # Generate signal
            self.generate_signal()

            # Push signals and paper signals to DB if not FLAT
            self.push_paper_signal()

            count += 1

            print(f"Paper Signals generated for {count}/1599 - {strategy}")

            if count == 1599:
                break
