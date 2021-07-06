import datetime

import pandas as pd
from django.test import TestCase
from django.utils.timezone import make_aware
from pandas_datareader import data as pdr
import yfinance as yf

from .companyquotes import CompanyQuotes

from strategies.models import Company
from strategies.models import TickerData

from papertrader.models import CurrentQuote

from services.Utils.pusher import Pusher

# Override default pandas data reader downloader

yf.pdr_override()


class CompanyQuotesTestCase(TestCase):
    def setUp(self) -> None:
        # create a company
        Company(name="TCS", ticker="TCS.NS", description="No description").save()
        Company(name="AXIS BANK", ticker="AXISBANK.NS", description="No description").save()

        # create dataframe for input
        self.df = pd.read_csv('/home/app/restapi/services/TCS_Yahoo_data.csv')
        self.df.drop(['Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)
        self.df['time_stamp'] = [time_stamp + " 00:00:00+00:00" for time_stamp in self.df['time_stamp']]

        # push Dummy company data to db
        self.company_df = self.df.copy()
        self.company_df['time_period'] = "1"
        self.company_df['company'] = Company.objects.all()[0]

        Pusher(df=self.company_df).push(TickerData)

    def test_inputs_none(self):
        """No inputs are given"""
        self.assertEquals(CompanyQuotes().companies, None)

    def test_all_inputs(self):
        """All inputs are given"""
        self.assertEquals(CompanyQuotes(companies=list(Company.objects.all())).companies, list(Company.objects.all()))

    def test_update_errors(self):
        """Checks if errors are raised if invalid inputs are given"""
        self.assertRaises(ValueError, CompanyQuotes(companies="abc").update)
        self.assertRaises(ValueError, CompanyQuotes(companies=[]).update)
        self.assertRaises(ValueError, CompanyQuotes(companies=["abc"]).update)
        self.assertRaises(ValueError, CompanyQuotes(companies=[list(Company.objects.all())[0], "abc"]).update)

    def test_validate_correct(self):
        """Checks if validate method updates companies list correctly"""
        # Ensure that all companies are taken if no input
        cq = CompanyQuotes()
        self.assertEquals(cq.companies, None)
        cq.validate()
        self.assertEquals(cq.companies, list(Company.objects.all()))

        # Ensure all companies are not taken if valid input list is provided
        cq = CompanyQuotes(companies=[list(Company.objects.all())[0]])
        self.assertEquals(cq.companies, [list(Company.objects.all())[0]])
        cq.validate()
        self.assertEquals(cq.companies, [list(Company.objects.all())[0]])

    def test_update_correct(self):
        """Checks if the update method works correctly"""
        CurrentQuote(
            company=Company.objects.all()[0],
            ticker_data=TickerData.objects.all()[len(TickerData.objects.all()) - 1],
            last_updated=make_aware(datetime.datetime.now())
        ).save()

        # Ensure that quote is updated if present in DB
        cq = CompanyQuotes(companies=[list(Company.objects.all())[0]])
        self.assertEquals(len(CurrentQuote.objects.all()), 1)
        cq.update()
        self.assertEquals(len(CurrentQuote.objects.all()), 1)

        # Ensure that new quote is added if a company doesn't have a quote in DB
        cq = CompanyQuotes()
        self.assertEquals(len(CurrentQuote.objects.all()), 1)
        cq.update()
        self.assertEquals(len(CurrentQuote.objects.all()), 2)
