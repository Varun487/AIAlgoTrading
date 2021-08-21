import datetime

import pandas as pd
from django.test import TestCase

from .bb_paper_trade_visualization import BBPaperTradeVisualization

from strategies.models import Company
from strategies.models import StrategyType
from strategies.models import StrategyConfig
from strategies.models import TickerData

from papertrader.models import PaperTrade
from papertrader.models import PaperTradedStrategy
from papertrader.models import CurrentQuote
from papertrader.models import PaperSignal

from backtester.models import BackTestReport
from backtester.models import BackTestTrade

from services.IndicatorCalc.indicators import BollingerIndicator
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.OrderExecution.orderexecution import OrderExecution
from services.TradeEvaluation.tradeevaluator import TradeEvaluator
from services.Utils.pusher import Pusher
from services.BackTestReportGeneration.backtestreportgenerator import BackTestReportGenerator

from services.PaperTradeSynchronizer.papertradesynchronizer import PaperTradeSynchronizer


class BBPaperTradeVisualizationTestCase(TestCase):
    def setUp(self) -> None:
        # create a company
        Company(name="TCS", ticker="TCS.NS", description="No description").save()

        # create dataframe to push to DB
        self.df = pd.read_csv('/home/app/restapi/services/TCS_Yahoo_data.csv')
        self.df.drop(['Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)
        self.df['time_stamp'] = [time_stamp + " 00:00:00+00:00" for time_stamp in self.df['time_stamp']]
        self.df['company'] = Company.objects.all()[0]

        # push all company data to db
        Pusher(df=self.df).push(TickerData)

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

        # Run backtest and generate report
        BackTestReportGenerator(
            df=self.df,
            ticker_time_period="1",
            indicator_time_period=5,
            dimension="close",
            sigma=1,
            factor=1,
            max_holding_period=5,
            company=Company.objects.all()[0],
            strategy_type=StrategyType.objects.all()[0],
            indicator=BollingerIndicator,
            strategy_config=StrategyConfig.objects.all()[0],
            signal_generator=BBSignalGenerator,
            take_profit_stop_loss=TakeProfitAndStopLossBB,
            order_executor=OrderExecution,
            trade_evaluator=TradeEvaluator,
        ).generate_backtest_report()

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

        PaperTradeSynchronizer(
            test_end_date=datetime.datetime(2021, 7, 8),
            test_today=datetime.datetime(2021, 7, 7)
        ).run()

        PaperTradeSynchronizer(
            test_end_date=datetime.datetime(2021, 7, 8),
            test_today=datetime.datetime(2021, 7, 7)
        ).run()

    def test_inputs_none(self):
        """No inputs are given"""
        self.assertEquals(BBPaperTradeVisualization().paper_trade, None)

    def test_all_inputs(self):
        """All inputs given"""
        # print(Company.objects.all())
        # print(TickerData.objects.all())
        # print(StrategyType.objects.all())
        # print(StrategyConfig.objects.all())
        # print(PaperTrade.objects.all())
        # print(PaperTradedStrategy.objects.all())
        # print(CurrentQuote.objects.all())
        # print(PaperSignal.objects.all())
        # print(PaperTrade.objects.all())

        self.assertEquals(BBPaperTradeVisualization(paper_trade=PaperTrade.objects.all()[0]).paper_trade,
                          PaperTrade.objects.all()[0])

    def test_generate_visualization_errors(self):
        """Checks if the generate_visualization method works correctly"""
        self.assertRaises(ValueError, BBPaperTradeVisualization(backtest_report=BackTestReport.objects.all()[0],
                                                                paper_trade="abc",
                                                                height=6, width=15).get_visualization)

    def test_generate_visualization(self):
        """Checks if the generate_visualization method works correctly"""
        # print(PaperTrade.objects.all()[0].trade.entry_order)
        # print(PaperTrade.objects.all()[0].trade.exit_order)
        # print(PaperTrade.objects.all()[0].trade.entry_order.ticker_data.time_stamp.date())

        self.assertEquals(type(BBPaperTradeVisualization(backtest_report=BackTestReport.objects.all()[0],
                                                         paper_trade=PaperTrade.objects.all()[0], height=6,
                                                         width=15).get_visualization()), str)
