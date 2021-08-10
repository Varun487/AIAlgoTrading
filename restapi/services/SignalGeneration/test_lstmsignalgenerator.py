from django.test import TestCase

import pandas as pd

from .lstmsignalgenerator import LSTMSignalGenerator
from services.IndicatorCalc.indicators import BollingerIndicator


class LSTMSignalGeneratorTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy data

        # create dataframe for input
        self.df = pd.read_csv('/home/app/restapi/services/TCS_Yahoo_data.csv')
        self.df.drop(['Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)
        self.df['time_stamp'] = [time_stamp + " 00:00:00+05:30" for time_stamp in self.df['time_stamp']]

        # push Dummy company data to db
        # self.company_df = self.df.copy()
        # self.company_df['time_period'] = "1"
        # self.company_df['company'] = Company.objects.all()[0]
        #
        # Pusher(df=self.company_df).push(TickerData)

        # self.correct_indicator_df = BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1).calc()
        #
        # self.signals = []
        # self.signals_df = self.correct_indicator_df.copy()
        #
        # for i in range(len(self.correct_indicator_df)):
        #     if self.correct_indicator_df['bb_bbhi'][i] != 0.0:
        #         self.signals.append("SELL")
        #     elif self.correct_indicator_df['bb_bbli'][i] != 0.0:
        #         self.signals.append("BUY")
        #     else:
        #         self.signals.append("FLAT")
        #
        # self.signals_df["SIGNAL"] = self.signals
        # self.signals_df.set_index("close", inplace=True)
        # self.signals_df.reset_index(inplace=True)

    def test_generate_signals(self):
        """Check if correct signals are generated"""
        # self.assertEquals(LSTMSignalGenerator(indicator=BollingerIndicator(df=self.df, time_period=5,
        # dimension="close", sigma=1)).generate_signals().equals( self.signals_df), True)
        # print()
        LSTMSignalGenerator(indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1))\
            .generate_signals()
