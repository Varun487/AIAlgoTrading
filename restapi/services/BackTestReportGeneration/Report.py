import pandas as pd

from services.Utils.converter import Converter
from services.Utils.pusher import push
from services.Utils.getters import get_data

class Report(object):

    def __init__(self, df=None):
        self.df = df
        self.valid_df = False
        self.valid = False

    def validate_df(self):
        return Converter(df=self.df).validate_df()

    def validate(self):
        self.valid_df = self.validate_df()

    def is_valid(self):
        self.validate()
        self.valid = self.valid_df


    def calc(self):
        self.is_valid()
        self.net_returns = 0
        self.entry_prices = 0
        self.net_percent = 0
        self.pf_trades = 0
        self.total_trades = 0
        if self.valid:
            for i in range(len(self.df)):
                self.net_returns = self.net_returns + self.df['net'][i]
                self.entry_prices = self.entry_prices + self.df['entry'][i]
                self.net_percent = (self.net_returns/self.entry_prices) *100
                if (self.df['trades'][i]>=0):
                    self.pf_trades += 1
                    self.total_trades +=self.df['trades'][i]


        else:
            raise TypeError("Inputs are invalid!")
