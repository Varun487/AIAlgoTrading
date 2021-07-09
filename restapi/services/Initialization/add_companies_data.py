import datetime

import pandas as pd
from django.utils.timezone import make_aware

from services.Utils.pusher import Pusher
from services.SourceData.sourcedata import SourceData

from strategies.models import Company
from strategies.models import TickerData


class AddCompaniesData(object):

    def __init__(self,  step=0, stop_point=1000):
        self.stop_point = stop_point
        self.step = step

        # Get all Nifty 50 companies
        self.df = pd.read_csv('/home/app/restapi/services/Initialization/nifty50list.csv')
        self.companies = list(Company.objects.all())
        self.number_of_companies = len(list(Company.objects.all()))
        self.company_df = None

    def run(self):
        count = 0

        # For each company
        for company in self.companies:
            count += 1
            print(f"    Sourcing data for company {count} of {self.number_of_companies}: {company.ticker}")

            # Source data
            self.company_df = SourceData(
                company=company,
                start_date=datetime.datetime(2017, 1, 1),
                end_date=datetime.datetime(2021, 1, 1),
            ).get_df()

            # Modify sourced data
            self.company_df.reset_index(inplace=True)
            self.company_df.rename(columns={
                'Date': 'time_stamp',
                'Open': 'open',
                'High': 'high',
                'Low': 'low',
                'Close': 'close',
                'Volume': 'volume',
            }, inplace=True)
            self.company_df['company'] = company
            self.company_df['time_period'] = '1'
            self.company_df['time_stamp'] = list(map(lambda x: make_aware(x), self.company_df['time_stamp']))
            self.company_df.dropna(inplace=True)
            self.company_df.reset_index(inplace=True)
            self.company_df.drop(['Adj Close', 'index'], axis=1, inplace=True)

            # Push ticker data to DB
            Pusher(df=self.company_df).push(TickerData)

            if count == self.stop_point:
                break

        print(f"STEP {self.step}: Added all companies data to DB")
