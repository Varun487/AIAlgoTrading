from django.test import TestCase

import pandas as pd

from .indicators import Indicator
from strategies.models import TickerData, Company
from strategies.models import IndicatorType

class IndicatorTestCase(TestCase):

    def setUp(self) -> None:
        # Dummy data
        # self.ticker_data = [TickerData(open=1.1, low=1.0, high=1.2, close=1.5 , volume =150 , timestamp= 2021-05-1,company= "TCS.BO", time_period= "1")]

        # self.ticker_open = [i.open for i in self.ticker_data]
        # self.ticker_low = [i.low for i in self.ticker_data]
        # self.ticker_high = [i.high for i in self.ticker_data]
        # self.ticker_close = [i.close for i in self.ticker_data]
        # self.ticker_volume = [i.volume for i in self.ticker_data]
        # self.ticker_time_stamp = [i.time_stamp for i in self.ticker_data]
        # self.ticker_time_period = [i.time_period for i in self.ticker_data]
        # self.dimension = [i.dimension for i in ["open","low","high","close"]]
        # self.dimension=f"{self.ticker_open}"|f"{self.ticker_close}"|f"{self.ticker_high}"|f"{self.ticker_low}"

        Company.objects.create(name='abc', ticker='ABC', description='desc')

        db_company = Company.objects.get(name='abc')
        
        df = pd.DataFrame()
        df["close"] = [134 , 245, 666, 290, 288.0]



    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(Indicator().dimension, "")
        self.assertEquals(Indicator().df, None)
        self.assertEquals(Indicator().time_period, -1)

    def test_input_df(self):
        """Only df is given as input"""
        # self.assertEquals(Indicator(df=self.ticker_data).time_period, -1)
        # self.assertEquals(Indicator(df=self.ticker_data).df.equals(self.ticker_data), True)
        # self.assertEquals(Indicator(df=self.ticker_data).dimension, "")
        print(df)

    # def test_input_time_period(self):
    #     """Only time period is given as input"""
    #     self.assertEquals(Indicator(time_period=self.ticker_time_period).time_period,self.ticker_time_period)
    #     self.assertEquals(Indicator(time_period=self.ticker_time_period).df,None)
    #     self.assertEquals(Indicator(time_period=self.ticker_time_period).dimension, "")

    # def test_input_dimension(self):
    #     """Only dimension is given as input"""
    #     self.assertEquals(Indicator(dimension=self.ticker_dimension).time_period,-1)
    #     self.assertEquals(Indicator(dimension=self.ticker_dimension).df, None)
    #     self.assertEquals(Indicator(dimension=self.ticker_dimension).dimension,self.dimension)

    # def test_input_both_df_and_time_period(self):
    #     """Both df and time period are given as input"""
    #     self.assertEquals(Indicator(df=self.ticker_data,time_period=self.ticker_time_period).time_period,self.ticker_time_period)
    #     self.assertEquals(Indicator(df=self.ticker_data, time_period=self.ticker_time_period).df.equals(self.ticker_data),True)




    # def test_input_both(self):
    #     """Both inputs are given"""
    #     self.assertEquals(Converter(df=self.company_df, obj_list=list(Company.objects.all())).obj_list, list(Company.objects.all()))
    #     self.assertEquals(Converter(df=self.company_df, obj_list=list(Company.object
    #
    # s.all())).df.equals(self.company_df), True)
    #
    # def test_to_df_obj_list_correct(self):
    #     """Conversion to dataframe is accurate"""
    #     self.assertEquals(Converter(obj_list=list(Company.objects.all())).to_df().equals(self.company_df), True)
    #     self.assertEquals(Converter(obj_list=list(IndicatorType.objects.all())).to_df().equals(self.indicator_type_df), True)
    #
    # def test_to_df_no_obj_list(self):
    #     """Check if the Value Error exception is raised for to_df"""
    #     self.assertRaises(ValueError, Converter(obj_list=[]).to_df)
    #     self.assertRaises(ValueError, Converter().to_df)
    #
    # def test_to_obj_list_correct(self):
    #     """Conversion to object list is accurate"""
    #     self.assertEquals(Converter(df=self.company_df).to_obj_list(Company), list(Company.objects.all()))
    #     self.assertEquals(Converter(df=self.indicator_type_df).to_obj_list(IndicatorType), list(IndicatorType.objects.all()))
    #
    # def test_to_obj_list_no_df(self):
    #     """Check if the Value Error exception is raised for to_obj_list"""
    #     self.assertRaises(ValueError, Converter(df=pd.DataFrame()).to_obj_list, Company)
    #     self.assertRaises(ValueError, Converter().to_obj_list, IndicatorType)
