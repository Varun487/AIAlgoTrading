import datetime

import pandas as pd
from django.test import TestCase

from strategies.models import Company
from strategies.models import TickerData
from strategies.models import StrategyConfig, StrategyType

from papertrader.models import PaperTradedStrategy
from papertrader.models import PaperSignal

from services.Utils.pusher import Pusher
from services.SourceData.sourcedata import SourceData

from .papersignalgenerator import PaperSignalGenerator


class PaperSignalGeneratorTestCase(TestCase):
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

    def test_end_date_values(self):
        self.assertEquals(
            PaperSignalGenerator(
                test_end_date=datetime.datetime(2021, 7, 8),
            ).end_date,
            datetime.datetime(2021, 7, 8)
        )
        self.assertEquals(
            PaperSignalGenerator().end_date,
            None
        )

        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[1], company=Company.objects.all()[0],
                            live=True).save()

        psg = PaperSignalGenerator()
        psg.run()
        self.assertEqual(psg.end_date.date(), datetime.datetime.today().date())

    def test_run(self):
        """Checks if signals are generated properly"""
        psg = PaperSignalGenerator(
            test_end_date=datetime.datetime(2021, 7, 8),
            test_today = datetime.datetime(2021, 7, 7),
        )

        # No live strategies
        psg.run()
        self.assertEquals(len(list(PaperSignal.objects.all())), 0)

        # Single live strategy, no signal produced
        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[0], company=Company.objects.all()[0],
                            live=True).save()
        psg.run()
        self.assertEquals(len(list(PaperSignal.objects.all())), 0)

        # 2 strategies, 1 live, 1 not live
        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[2], company=Company.objects.all()[0],
                            live=False).save()
        psg.run()
        self.assertEquals(len(list(PaperSignal.objects.all())), 0)

        # 3 strategies, 2 live, 1 signal generated
        PaperTradedStrategy(strategy_config=StrategyConfig.objects.all()[1], company=Company.objects.all()[0],
                            live=True).save()
        psg.run()
        self.assertEquals(len(list(PaperSignal.objects.all())), 1)
