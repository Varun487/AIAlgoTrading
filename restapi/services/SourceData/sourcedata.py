import datetime
from pandas_datareader import data as pdr
import yfinance as yf

from strategies.models import Company

# Override default pandas data reader downloader for yahoo finance
yf.pdr_override()


class SourceData(object):
    """Used to source company data, both real time and historical"""

    def __init__(self, company=None, start_date=None, end_date=None):
        self.df = None
        self.company = company
        self.start_date = start_date
        self.end_date = end_date

        self.valid_company = False
        self.valid_start_date = False
        self.valid_end_date = False
        self.valid = False

    def validate_company(self):
        self.valid_company = isinstance(self.company, Company)

    def validate_dates(self):
        self.valid_end_date = isinstance(self.end_date, datetime.datetime)
        self.valid_start_date = isinstance(self.start_date, datetime.datetime)

    def validate(self):
        self.validate_company()
        self.validate_dates()
        self.valid = self.valid_company and self.valid_start_date and self.valid_end_date

    def source(self):
        self.df = pdr.get_data_yahoo(self.company.ticker, start=self.start_date, end=self.end_date, progress=False)

    def get_df(self):
        self.validate()
        if self.valid:
            self.source()
            return self.df
        else:
            raise ValueError("The inputs given are invalid!")
