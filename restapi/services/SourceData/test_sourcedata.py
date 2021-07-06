from django.utils.timezone import make_aware
from django.test import TestCase
from pandas_datareader import data as pdr
import datetime
import yfinance as yf

from .sourcedata import SourceData

from strategies.models import Company

# Override default pandas data reader downloader
yf.pdr_override()


class SourceDataTestCase(TestCase):
    def setUp(self) -> None:
        # Set up dates
        self.start_date = make_aware(datetime.datetime.now() - datetime.timedelta(days=5))
        self.end_date = make_aware(datetime.datetime.now())

        # Source latest data for TCS.NS
        self.df = pdr.get_data_yahoo('TCS.NS', start=self.start_date, end=self.end_date, progress=False)

        # create a company
        Company(name="TCS", ticker="TCS.NS", description="No description").save()

    def test_inputs_none(self):
        """No inputs are given"""
        self.assertEquals(SourceData().df, None)
        self.assertEquals(SourceData().company, None)
        self.assertEquals(SourceData().start_date, None)
        self.assertEquals(SourceData().end_date, None)

    def test_all_inputs(self):
        """All inputs given as input"""
        self.assertEquals(SourceData(company=Company.objects.all()[0]).company, Company.objects.all()[0])
        self.assertEquals(SourceData(start_date=self.start_date).start_date, self.start_date)
        self.assertEquals(SourceData(end_date=self.end_date).end_date, self.end_date)

    def test_get_df_errors(self):
        """Checks if errors are raised if invalid inputs are given"""
        self.assertRaises(ValueError, SourceData(company=Company.objects.all()[0]).get_df)
        self.assertRaises(ValueError, SourceData(start_date=self.start_date).get_df)
        self.assertRaises(ValueError, SourceData(end_date=self.end_date).get_df)

        self.assertRaises(ValueError, SourceData(start_date=self.start_date, end_date=self.end_date).get_df)
        self.assertRaises(ValueError, SourceData(company=Company.objects.all()[0], end_date=self.end_date).get_df)
        self.assertRaises(ValueError, SourceData(company=Company.objects.all()[0], start_date=self.start_date).get_df)

        self.assertRaises(ValueError, SourceData(company="abc", start_date=self.start_date,
                                                 end_date=self.end_date).get_df)
        self.assertRaises(ValueError, SourceData(company=Company.objects.all()[0], start_date="abc",
                                                 end_date=self.end_date).get_df)
        self.assertRaises(ValueError, SourceData(company=Company.objects.all()[0], start_date=self.start_date,
                                                 end_date="abc").get_df)

    def test_get_df_correct(self):
        """Checks if the get_df method works correctly"""
        self.assertEquals(SourceData(company=Company.objects.all()[0], start_date=self.start_date,
                                     end_date=self.end_date).get_df().equals(self.df), True)
