from django.test import TestCase

import pandas as pd

from .indicators import Indicator
from strategies.models import TickerData, Company
from strategies.models import IndicatorType


class IndicatorTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy data
        Company.objects.create(name='abc', ticker='ABC', description='desc')

        self.db_company = Company.objects.get(name='abc')

        self.df = pd.DataFrame()
        self.df["close"] = [134, 245, 666, 290, 288.0]

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(Indicator().dimension, "")
        self.assertEquals(Indicator().df, None)
        self.assertEquals(Indicator().time_period, -1)

    def test_input_df(self):
        """Only df is given as input"""
        print(self.df)
