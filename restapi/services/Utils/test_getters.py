from django.test import TestCase

import pandas as pd

from .getters import Getter
from .converter import Converter

from strategies.models import Company
from strategies.models import IndicatorType


class GetDataTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy company data
        Company.objects.create(name='abc', ticker='ABC', description='desc')
        Company.objects.create(name='abcd', ticker='ABCD', description='desc')
        Company.objects.create(name='abce', ticker='ABCE', description='desc')

        # Dummy indicator data
        IndicatorType.objects.create(name='abc', description='desc')
        IndicatorType.objects.create(name='abcd', description='desc')
        IndicatorType.objects.create(name='abce', description='desc')

        self.param_list_company = {"name": "abc", "ticker": 'ABC', "description": 'desc'}
        self.param_list_indicator_type = {"name": "abc", "description": 'desc'}

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(Getter().table_name, None)
        self.assertEquals(Getter().param_list, None)
        self.assertEquals(Getter().df_flag, False)

    def test_input_all(self):
        """All inputs provided"""
        self.assertEquals(Getter(table_name=Company, df_flag=True, param_list=self.param_list_company).table_name,
                          Company)
        self.assertEquals(Getter(table_name=Company, df_flag=True, param_list=self.param_list_company).param_list,
                          self.param_list_company)
        self.assertEquals(Getter(table_name=Company, df_flag=True, param_list=self.param_list_company).df_flag, True)

    def test_input_df_flag(self):
        """Only df_flag input is provided"""
        self.assertEquals(Getter(df_flag=True).df_flag, True)
        self.assertEquals(Getter(df_flag=False).df_flag, False)

    def test_get_data_correct_obj_list(self):
        """Whether it returns correct obj list when input is correct"""
        # Returns correct object list for company
        self.assertEquals(Getter(table_name=Company, df_flag=False, param_list=self.param_list_company).get_data(),
                          list(Company.objects.filter(**self.param_list_company)))
        self.assertEquals(Getter(table_name=Company, param_list={"description": 'desc'}).get_data(),
                          list(Company.objects.filter(**{"description": 'desc'})))
        self.assertEquals(Getter(table_name=Company, param_list={"name": "abcd"}).get_data(),
                          list(Company.objects.filter(**{"name": "abcd"})))

        # Returns correct object list for Indicator
        self.assertEquals(
            Getter(table_name=IndicatorType, df_flag=False, param_list=self.param_list_indicator_type).get_data(),
            list(IndicatorType.objects.filter(**self.param_list_indicator_type)))
        self.assertEquals(Getter(table_name=IndicatorType, param_list={"description": 'desc'}).get_data(),
                          list(IndicatorType.objects.filter(**{"description": 'desc'})))
        self.assertEquals(Getter(table_name=IndicatorType, param_list={"name": "abcd"}).get_data(),
                          list(IndicatorType.objects.filter(**{"name": "abcd"})))

    def test_get_data_correct_df(self):
        """Whether it returns correct df when input is correct"""
        # Returns correct df for company
        self.assertEquals(Getter(table_name=Company, df_flag=True, param_list=self.param_list_company).get_data()
            .equals(
            Converter(obj_list=list(Company.objects.filter(**self.param_list_company))).to_df()
        ), True)
        self.assertEquals(Getter(table_name=Company, df_flag=True, param_list={"description": 'desc'}).get_data()
            .equals(
            Converter(obj_list=list(Company.objects.filter(**{"description": 'desc'}))).to_df()
        ), True)
        self.assertEquals(Getter(table_name=Company, df_flag=True, param_list={"name": "abcd"}).get_data()
            .equals(
            Converter(obj_list=list(Company.objects.filter(**{"name": "abcd"}))).to_df()
        ), True)

        # Returns correct df for indicator type
        self.assertEquals(
            Getter(table_name=IndicatorType, df_flag=True, param_list=self.param_list_indicator_type).get_data()
                .equals(
                Converter(obj_list=list(IndicatorType.objects.filter(**self.param_list_indicator_type))).to_df()
            ), True)
        self.assertEquals(Getter(table_name=IndicatorType, df_flag=True, param_list={"description": 'desc'}).get_data()
            .equals(
            Converter(obj_list=list(IndicatorType.objects.filter(**{"description": 'desc'}))).to_df()
        ), True)
        self.assertEquals(Getter(table_name=IndicatorType, df_flag=True, param_list={"name": "abcd"}).get_data()
            .equals(
            Converter(obj_list=list(IndicatorType.objects.filter(**{"name": "abcd"}))).to_df()
        ), True)

    def test_get_data_invalid_inputs(self):
        self.assertRaises(TypeError,
                          Getter(table_name="IndicatorTyp", df_flag=True, param_list={"name": "abcd"}).get_data)
        self.assertRaises(TypeError, Getter(table_name=IndicatorType, param_list={"nam": "abcd"}).get_data)
        self.assertRaises(TypeError, Getter(table_name=Company, param_list={"name": "abcd", "res": "abcd"}))
