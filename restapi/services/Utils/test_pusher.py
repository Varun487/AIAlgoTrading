from django.test import TestCase
import pandas as pd

from .pusher import Pusher

from strategies.models import Company
from strategies.models import IndicatorType


class PushersTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy company data
        self.company_data = [Company(name='abc', ticker='ABC', description='desc'),
                             Company(name='abcd', ticker='ABCD', description='desc'),
                             Company(name='abce', ticker='ABCE', description='desc')]

        self.company_names = [i.name for i in self.company_data]
        self.company_tickers = [i.ticker for i in self.company_data]
        self.company_descriptions = [i.description for i in self.company_data]

        # Dataframe for company data
        self.company_df = pd.DataFrame({"name": self.company_names,
                                        "ticker": self.company_tickers,
                                        "description": self.company_descriptions})

        # Dummy indicator data
        IndicatorType.objects.create(name='abc', description='desc')
        IndicatorType.objects.create(name='abcd', description='desc')
        IndicatorType.objects.create(name='abce', description='desc')

        # To build the data frame
        self.indicator_type_ids = [i.id for i in IndicatorType.objects.all()]
        self.indicator_type_names = [i.name for i in IndicatorType.objects.all()]
        self.indicator_type_descriptions = [i.description for i in IndicatorType.objects.all()]

        # Dataframe for Indicator Type data
        self.indicator_type_df = pd.DataFrame({"id": self.indicator_type_ids,
                                               "name": self.indicator_type_names,
                                               "description": self.indicator_type_descriptions})

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(Pusher().obj_list, None)
        self.assertEquals(Pusher().df, None)

    def test_input_df(self):
        """Only df is given as input"""
        self.assertEquals(Pusher(df=self.company_df).obj_list, None)
        self.assertEquals(Pusher(df=self.company_df).df.equals(self.company_df), True)

    def test_input_obj_list(self):
        """Only obj_list is given as input"""
        self.assertEquals(Pusher(obj_list=self.company_data).obj_list, self.company_data)
        self.assertEquals(Pusher(obj_list=self.company_data).df, None)

    def test_input_both(self):
        """Both inputs are given"""
        self.assertEquals(Pusher(df=self.company_df, obj_list=self.company_data).obj_list, self.company_data)
        self.assertEquals(Pusher(df=self.company_df, obj_list=self.company_data).df.equals(self.company_df), True)

    def test_get_obj_list(self):
        """Test whether the data from get object list is correct"""
        self.assertEquals(Pusher(obj_list=self.company_data).get_obj_list(Company), self.company_data)

        converted_company_obj_list = Pusher(df=self.company_df).get_obj_list(Company)
        company_names = [i.name for i in converted_company_obj_list]
        company_tickers = [i.ticker for i in converted_company_obj_list]
        company_descriptions = [i.description for i in converted_company_obj_list]

        self.assertEquals(company_names, self.company_names)
        self.assertEquals(company_tickers, self.company_tickers)
        self.assertEquals(company_descriptions, self.company_descriptions)

    # def test_pusher(self):
    #     converted_company_obj_list = Pusher(df=self.company_df).get_obj_list(Company)
    #     company_names = [i.name for i in converted_company_obj_list]
    #     company_tickers = [i.ticker for i in converted_company_obj_list]
    #     company_descriptions = [i.description for i in converted_company_obj_list]
    #     Pusher(obj_list=self.company_data).push(Company)
    #     self.assertEquals(Company.objects.all())
    #     self.assertEquals(Pusher()
    #
