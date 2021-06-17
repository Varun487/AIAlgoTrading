from django.test import TestCase

import pandas as pd

from .converter import Converter

from strategies.models import Company
from strategies.models import IndicatorType


class ConvertersTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy company data
        Company.objects.create(name='abc', ticker='ABC', description='desc')
        Company.objects.create(name='abcd', ticker='ABCD', description='desc')
        Company.objects.create(name='abce', ticker='ABCE', description='desc')

        self.company_ids = [i.id for i in Company.objects.all()]
        self.company_names = [i.name for i in Company.objects.all()]
        self.company_tickers = [i.ticker for i in Company.objects.all()]
        self.company_descriptions = [i.description for i in Company.objects.all()]

        # Dataframe for company data
        self.company_df = pd.DataFrame({"id": self.company_ids,
                                        "name": self.company_names,
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
        self.assertEquals(Converter().obj_list, None)
        self.assertEquals(Converter().df, None)

    def test_input_df(self):
        """Only df is given as input"""
        self.assertEquals(Converter(df=self.company_df).obj_list, None)
        self.assertEquals(Converter(df=self.company_df).df.equals(self.company_df), True)

    def test_input_obj_list(self):
        """Only obj_list is given as input"""
        self.assertEquals(Converter(obj_list=list(Company.objects.all())).obj_list, list(Company.objects.all()))
        self.assertEquals(Converter(obj_list=list(Company.objects.all())).df, None)

    def test_input_both(self):
        """Both inputs are given"""
        self.assertEquals(Converter(df=self.company_df, obj_list=list(Company.objects.all())).obj_list, list(Company.objects.all()))
        self.assertEquals(Converter(df=self.company_df, obj_list=list(Company.objects.all())).df.equals(self.company_df), True)

    def test_to_df_obj_list_correct(self):
        """Conversion to dataframe is accurate"""
        self.assertEquals(Converter(obj_list=list(Company.objects.all())).to_df().equals(self.company_df), True)
        self.assertEquals(Converter(obj_list=list(IndicatorType.objects.all())).to_df().equals(self.indicator_type_df), True)

    def test_to_df_no_obj_list(self):
        """Check if the Value Error exception is raised for to_df"""
        self.assertRaises(ValueError, Converter(obj_list=[]).to_df)
        self.assertRaises(ValueError, Converter().to_df)

    def test_to_obj_list_correct(self):
        """Conversion to object list is accurate"""
        self.assertEquals(Converter(df=self.company_df).to_obj_list(Company), list(Company.objects.all()))
        self.assertEquals(Converter(df=self.indicator_type_df).to_obj_list(IndicatorType), list(IndicatorType.objects.all()))

    def test_to_obj_list_no_df(self):
        """Check if the Value Error exception is raised for to_obj_list"""
        self.assertRaises(ValueError, Converter(df=pd.DataFrame()).to_obj_list, Company)
        self.assertRaises(ValueError, Converter().to_obj_list, IndicatorType)
