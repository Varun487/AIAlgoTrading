import pandas as pd

from services.Utils.pusher import Pusher

from strategies.models import Company


class AddCompanies(object):
    def __init__(self, step=0):
        self.step = step

        # Get all Nifty 50 companies
        self.df = pd.read_csv('/home/app/restapi/services/Initialization/nifty50list.csv')

    def run(self):
        # Modify DB to push
        self.df.rename(columns={'Company Name': 'name', 'Industry': 'description', 'Symbol': 'ticker'}, inplace=True)
        self.df.drop(['Series', 'ISIN Code'], axis=1, inplace=True)
        self.df['ticker'] += ".NS"

        # Push data to DB
        Pusher(df=self.df).push(Company)

        print(f"STEP {self.step}: Added all companies to DB")
