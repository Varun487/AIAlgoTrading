import pandas as pd
import sys
from math import isnan
from services.Utils.converter import Converter
from ta.utils import dropna
from ta.volatility import BollingerBands

class Indicator(object):

    def __init__(self, df=None, time_period = -1, dimension = ""):
        self.df = df
        self.time_period = time_period
        self.dimension = dimension
        self.calc_df = None
        self.valid_df = False
        self.valid_time_period = False
        self.valid_dimension = False

    def validate_df(self):
        return Converter(df=self.df).validate_df()

    def validate_time_period(self):
        return (type(self.time_period) == int) and (self.time_period > 0)

    def validate_dimension(self):
        return (self.dimension in ["open","low","high","close"])

    def validate(self):
        self.valid_df = self.validate_df()
        self.valid_time_period = self.validate_time_period()
        self.valid_dimension = self.validate_dimension()

    def is_valid(self):
        self.validate()
        return self.valid_df and self.valid_time_period and self.valid_dimension

    def business_logic(self):
        pass

    def calc(self):
        if self.is_valid():
            return self.business_logic()

class Bollinger(Indicator):
    def business_logic(self):
        # Initialize Bollinger Bands Indicator
        indicator_bb = BollingerBands(close=self.df["Close"], window=20, window_dev=2)

        # Add Bollinger Bands features
        self.df['bb_bbm'] = indicator_bb.bollinger_mavg()
        self.df['bb_bbh'] = indicator_bb.bollinger_hband()
        self.df['bb_bbl'] = indicator_bb.bollinger_lband()

        # Add Bollinger Band high indicator
        self.df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()

        # Add Bollinger Band low indicator
        self.df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()

        return self.df, self.dimension
