from django.test import TestCase

import pandas as pd

from .indicators import BollingerIndicator, Indicator
from ta.volatility import BollingerBands


class IndicatorTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy data
        self.df = pd.DataFrame()
        self.df["close"] = [i for i in range(100, 1000, 5)]

        self.df = pd.DataFrame()
        self.df["close"] = [134, 245, 666, 290, 288.0]

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(Indicator().dimension, "")
        self.assertEquals(Indicator().df, None)
        self.assertEquals(Indicator().time_period, -1)

    def test_input_df(self):
        """Only df is given as input"""
        self.assertEquals(Indicator(df=self.df).time_period, -1)
        self.assertEquals(Indicator(df=self.df).df.equals(self.df), True)
        self.assertEquals(Indicator(df=self.df).dimension, "")

    def test_input_time_period(self):
        """Only time period is given as input"""
        self.assertEquals(Indicator(time_period=5).time_period, 5)
        self.assertEquals(Indicator(time_period=5).df, None)
        self.assertEquals(Indicator(time_period=5).dimension, "")

    def test_input_dimension(self):
        """Only dimension is given as input"""
        self.assertEquals(Indicator(dimension="close").time_period, -1)
        self.assertEquals(Indicator(dimension="close").df, None)
        self.assertEquals(Indicator(dimension="close").dimension, "close")

    def test_input_all(self):
        """All inputs are given"""
        self.assertEquals(Indicator(dimension="close", time_period=5, df=self.df).time_period, 5)
        self.assertEquals(Indicator(dimension="close", time_period=5, df=self.df).df.equals(self.df), True)
        self.assertEquals(Indicator(dimension="close", time_period=5, df=self.df).dimension, "close")

    def test_calc(self):
        """Tests Calc method"""
        self.assertEquals(Indicator(dimension="close", time_period=5, df=self.df).calc().equals(self.df), True)
        self.assertRaises(TypeError, Indicator(dimension="clse", time_period=5, df=self.df).calc)
        self.assertRaises(TypeError, Indicator(dimension="close", time_period=0, df=self.df).calc)
        self.assertRaises(TypeError, Indicator(dimension="close", time_period=5, df="kjk").calc)
        self.assertRaises(TypeError, Indicator(dimension="close", time_period=-3, df=self.df).calc)


class BollingerIndicatorTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy data
        self.df = pd.DataFrame()
        self.df["close"] = [i for i in range(100, 1000, 5)]
        indicator_bb = BollingerBands(close=self.df["close"], window=5, window_dev=2)

        self.compare_df = pd.DataFrame()
        self.compare_df["close"] = [i for i in range(100, 1000, 5)]

        # Add Bollinger Bands features
        self.compare_df['bb_bbm'] = indicator_bb.bollinger_mavg()
        self.compare_df['bb_bbh'] = indicator_bb.bollinger_hband()
        self.compare_df['bb_bbl'] = indicator_bb.bollinger_lband()

        # Add Bollinger Band high indicator
        self.compare_df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()

        # Add Bollinger Band low indicator
        self.compare_df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()
        self.compare_df = self.compare_df.dropna()
        self.compare_df.set_index(["close"], inplace=True)
        self.compare_df.reset_index(inplace=True)

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(BollingerIndicator().sigma, -1)

    def test_input_sigma(self):
        self.assertEquals(BollingerIndicator(sigma=2).sigma, 2)

    def test_calc(self):
        self.assertRaises(TypeError, BollingerIndicator(dimension="close", time_period=-3, df=self.df, sigma=2).calc)
        self.assertRaises(TypeError, BollingerIndicator(dimension="clse", time_period=5, df=self.df, sigma=2).calc)
        self.assertRaises(TypeError, BollingerIndicator(dimension="close", time_period=5, df="jj", sigma=2).calc)
        self.assertRaises(TypeError, BollingerIndicator(dimension="close", time_period=5, df=self.df, sigma=-2).calc)
        self.assertRaises(TypeError, BollingerIndicator(dimension="close", time_period=5, df=self.df, sigma=0).calc)
        self.assertEquals(
            BollingerIndicator(dimension="close", time_period=5, df=self.df, sigma=2).calc().equals(self.compare_df),
            True)
