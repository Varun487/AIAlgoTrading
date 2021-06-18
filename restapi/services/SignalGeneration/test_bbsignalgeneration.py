from django.test import TestCase

import pandas as pd

from .bbsignalgeneration import BBSignalGenerator
from services.IndicatorCalc.indicators import BollingerIndicator

class BBSignalGeneratorTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy data
        self.df = pd.DataFrame()
        self.df["close"] = [3114.00, 3158.50, 3180.00, 3143.60, 3159.15, 3153.00, 3129.45, 3141.25, 3143.75, 3183.20, 3200.15]

        self.correct_indicator_df = BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1).calc()

        self.signals = []
        self.signals_df = self.correct_indicator_df.copy()

        for i in range(len(self.correct_indicator_df)):
            if self.correct_indicator_df['bb_bbhi'][i] != 0.0:
                self.signals.append("SELL")
            elif self.correct_indicator_df['bb_bbli'][i] != 0.0:
                self.signals.append("BUY")
            else:
                self.signals.append("FLAT")

        self.signals_df["SIGNAL"] = self.signals
        self.signals_df.set_index("close", inplace=True)
        self.signals_df.reset_index(inplace=True)

    def test_generate_signals(self):
        """Check if correct signals are generated"""
        self.assertEquals(BBSignalGenerator(indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1)).generate_signals().equals(self.signals_df), True)
