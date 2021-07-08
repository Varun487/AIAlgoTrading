import datetime

import pandas as pd
from django.test import TestCase

from services.Utils.pusher import Pusher

from strategies.models import Company
from strategies.models import StrategyConfig, StrategyType
from strategies.models import TickerData

from papertrader.models import PaperTradedStrategy

from .papertradesynchronizer import PaperTradeSynchronizer
from papertrader.models import PaperTrade
from papertrader.models import PaperSignal
from papertrader.models import CurrentQuote


class PaperTradeSynchronizerTestCase(TestCase):
    def setUp(self) -> None:
        # create a company
        Company(name="TCS", ticker="TCS.NS", description="No description").save()

        # create dataframe for input
        self.df = pd.read_csv('/home/app/restapi/services/TCS_Yahoo_data.csv')
        self.df.drop(['Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)
        self.df['time_stamp'] = [time_stamp + " 00:00:00+05:30" for time_stamp in self.df['time_stamp']]

        # push Dummy company data to db
        self.company_df = self.df.copy()
        self.company_df['time_period'] = "1"
        self.company_df['company'] = Company.objects.all()[0]

        Pusher(df=self.company_df).push(TickerData)

        StrategyType(name="Simple Bollinger Band Strategy", description="NA", stock_selection="NA", entry_criteria="NA",
                     exit_criteria="NA", stop_loss_method="NA", take_profit_method="NA").save()

        StrategyConfig(strategy_type=StrategyType.objects.all()[0], indicator_time_period=5, max_holding_period=5,
                       take_profit_factor=1, stop_loss_factor=1, sigma=1, dimension="1").save()
        StrategyConfig(strategy_type=StrategyType.objects.all()[0], indicator_time_period=10, max_holding_period=5,
                       take_profit_factor=1, stop_loss_factor=1, sigma=1, dimension="1").save()
        StrategyConfig(strategy_type=StrategyType.objects.all()[0], indicator_time_period=20, max_holding_period=5,
                       take_profit_factor=1, stop_loss_factor=1, sigma=1, dimension="1").save()
        StrategyConfig(strategy_type=StrategyType.objects.all()[0], indicator_time_period=5, max_holding_period=5,
                       take_profit_factor=1, stop_loss_factor=1, sigma=2, dimension="1").save()
        StrategyConfig(strategy_type=StrategyType.objects.all()[0], indicator_time_period=10, max_holding_period=5,
                       take_profit_factor=1, stop_loss_factor=1, sigma=2, dimension="1").save()
        StrategyConfig(strategy_type=StrategyType.objects.all()[0], indicator_time_period=20, max_holding_period=5,
                       take_profit_factor=1, stop_loss_factor=1, sigma=2, dimension="1").save()

        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[0], company=Company.objects.all()[0],
                            live=True).save()
        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[1], company=Company.objects.all()[0],
                            live=True).save()
        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[2], company=Company.objects.all()[0],
                            live=True).save()
        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[3], company=Company.objects.all()[0],
                            live=True).save()
        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[4], company=Company.objects.all()[0],
                            live=True).save()
        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[5], company=Company.objects.all()[0],
                            live=True).save()

    def test_run(self):
        """Checks if all services work together in paper trade synchronizer"""
        self.assertEquals(len(list(CurrentQuote.objects.all())), 0)
        self.assertEquals(len(list(PaperSignal.objects.all())), 0)
        self.assertEquals(len(list(PaperTrade.objects.all())), 0)

        PaperTradeSynchronizer(
            test_end_date=datetime.datetime(2021, 7, 8),
            test_today=datetime.datetime(2021, 7, 7)
        ).run()

        self.assertEquals(len(list(CurrentQuote.objects.all())), 1)
        self.assertEquals(len(list(PaperSignal.objects.all())), 1)
        self.assertEquals(len(list(PaperTrade.objects.all())), 0)

        PaperTradeSynchronizer(
            test_end_date=datetime.datetime(2021, 7, 8),
            test_today=datetime.datetime(2021, 7, 7)
        ).run()

        self.assertEquals(len(list(CurrentQuote.objects.all())), 1)
        self.assertEquals(len(list(PaperSignal.objects.all())), 2)
        self.assertEquals(len(list(PaperTrade.objects.all())), 1)
