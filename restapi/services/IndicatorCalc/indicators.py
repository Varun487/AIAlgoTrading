from services.Utils.converter import Converter
from ta.volatility import BollingerBands


class Indicator(object):

    def __init__(self, df=None, time_period=-1, dimension=""):
        self.df = df
        self.time_period = time_period
        self.dimension = dimension
        self.calc_df = None
        self.valid_df = False
        self.valid_time_period = False
        self.valid_dimension = False
        self.valid = False

    def validate_df(self):
        return Converter(df=self.df).validate_df()

    def validate_time_period(self):
        return (type(self.time_period) == int) and (self.time_period > 0)

    def validate_dimension(self):
        return self.dimension in ["open", "low", "high", "close"]

    def validate(self):
        self.valid_df = self.validate_df()
        self.valid_time_period = self.validate_time_period()
        self.valid_dimension = self.validate_dimension()

    def is_valid(self):
        self.validate()
        self.valid = self.valid_df and self.valid_time_period and self.valid_dimension

    def business_logic(self):
        return self.df

    def calc(self):
        self.is_valid()
        if self.valid:
            return self.business_logic()
        else:
            raise TypeError("Inputs are invalid!")


class BollingerIndicator(Indicator):

    def __init__(self, df=None, time_period=-1, dimension="", sigma=-1):
        super().__init__(df, time_period, dimension)
        self.sigma = sigma
        self.valid_sigma = False

    def validate_sigma(self):
        return (type(self.sigma) == int) and (self.sigma > 0)

    def validate(self):
        super().validate()
        self.valid_sigma = self.validate_sigma()

    def is_valid(self):
        super().is_valid()
        self.valid = self.valid and self.valid_sigma

    def business_logic(self):
        # Initialize Bollinger Bands Indicator
        indicator_bb = BollingerBands(close=self.df[self.dimension], window=self.time_period, window_dev=self.sigma)

        # Add Bollinger Bands features
        self.df['bb_bbm'] = indicator_bb.bollinger_mavg()
        self.df['bb_bbh'] = indicator_bb.bollinger_hband()
        self.df['bb_bbl'] = indicator_bb.bollinger_lband()

        # Add Bollinger Band high indicator
        self.df['bb_bbhi'] = indicator_bb.bollinger_hband_indicator()

        # Add Bollinger Band low indicator
        self.df['bb_bbli'] = indicator_bb.bollinger_lband_indicator()

        self.df = self.df.dropna()
        self.df.set_index([self.dimension], inplace=True)
        self.df.reset_index(inplace=True)

        return self.df
