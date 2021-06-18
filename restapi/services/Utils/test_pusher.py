from django.test import TestCase
import pandas as pd

from .pusher import Pusher

from strategies.models import Company


def convert_to_dicts(obj_list):
    processed_list = [i.__dict__ for i in obj_list]

    for i in processed_list:
        i.pop("id", None)
        i.pop("_state", None)

    return processed_list


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

        self.incorrect_company_data = [Company(name='abc', description='desc'),
                                       Company(ticker='ABCD'),
                                       Company(name='abce', ticker='ABCE', description='desc')]

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

    def test_pusher(self):
        """Ensure data is pushed properly to DB"""
        # pushing data correctly
        self.assertEquals(list(Company.objects.all()), [])
        Pusher(df=self.company_df).push(Company)
        data_in_db = convert_to_dicts(list(Company.objects.all()))
        pushed_data = convert_to_dicts(self.company_data)
        self.assertEquals(data_in_db, pushed_data)

        # pushing same data multiple times
        Pusher(df=self.company_df).push(Company)
        prev_data_in_db = data_in_db
        current_data_in_db = convert_to_dicts(list(Company.objects.all()))
        self.assertEquals(prev_data_in_db, current_data_in_db)

        # Pushing incorrect objects
        self.assertRaises(ValueError, Pusher(obj_list=self.incorrect_company_data).push, Company)
