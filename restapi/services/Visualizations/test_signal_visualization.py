import pandas as pd
from django.test import TestCase

from .signal_visualization import SignalVisualization

from strategies.models import Company
from strategies.models import StrategyType
from strategies.models import StrategyConfig
from strategies.models import TickerData

from backtester.models import BackTestReport

from services.IndicatorCalc.indicators import BollingerIndicator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.OrderExecution.orderexecution import OrderExecution
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from services.TradeEvaluation.tradeevaluator import TradeEvaluator
from services.Utils.pusher import Pusher
from services.BackTestReportGeneration.backtestreportgenerator import BackTestReportGenerator


class SignalVisualizationTestCase(TestCase):
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

        # create a test strategy type
        StrategyType(name="Test", description="Test desc.", stock_selection="Test", entry_criteria="Test",
                     exit_criteria="Test", stop_loss_method="Test", take_profit_method="Test").save()

        # create a test strategy configuration
        StrategyConfig(strategy_type=StrategyType.objects.all()[0], indicator_time_period=5, max_holding_period=5,
                       take_profit_factor=1, stop_loss_factor=1, sigma=1, dimension="1").save()

        # push all company data to db
        Pusher(df=self.df).push(TickerData)

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

    def test_generate_visualization(self):
        """Checks if the generate_visualization method works correctly"""
        self.assertEquals(type(SignalVisualization(backtest_report=BackTestReport.objects.all()[0], height=6, width=15)
                          .generate_visualization()), str)
