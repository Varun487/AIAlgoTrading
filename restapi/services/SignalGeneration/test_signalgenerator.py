from django.test import TestCase

import pandas as pd

from services.IndicatorCalc.indicators import BollingerIndicator, Indicator
from services.Utils.test_pusher import convert_to_dicts
from .signalgenerator import SignalGenerator


class SignalGeneratorTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy data
        self.df = pd.DataFrame()
        self.df["close"] = [i for i in range(100, 1000, 5)]

        self.correct_indicator_df = BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=2).calc()

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(SignalGenerator().indicator, None)

    def test_input_indicator(self):
        """Indicator obj is given as input"""
        self.assertEquals(
            convert_to_dicts([SignalGenerator(indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close",sigma=2)).indicator]),
            convert_to_dicts([BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=2)])
        )

    def test_set_indicator_df(self):
        correct_signal_gen = SignalGenerator(indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=2))
        correct_signal_gen.set_indicator_df()
        self.assertEquals(correct_signal_gen.indicator_df.equals(self.correct_indicator_df), True)

        self.assertRaises(TypeError, SignalGenerator(indicator=BollingerIndicator(df=self.df, dimension="close", sigma=2)).set_indicator_df)
        self.assertRaises(TypeError, SignalGenerator(indicator=BollingerIndicator()).set_indicator_df)
        self.assertRaises(TypeError, SignalGenerator(indicator=BollingerIndicator(dimension="close", sigma=2)).set_indicator_df)
        self.assertRaises(TypeError, SignalGenerator(indicator=BollingerIndicator(time_period=5, dimension="close", sigma=2)).set_indicator_df)
        self.assertRaises(TypeError, SignalGenerator(indicator=BollingerIndicator(time_period=-1, dimension="close", sigma=2)).set_indicator_df)

    def test_get_signals(self):
        self.assertEquals(SignalGenerator(indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=2)).get_signals()
                          .equals(self.correct_indicator_df), True)
