import pandas as pd
from django.test import TestCase

from .visualization import Visualization

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


class VisualizationTestCase(TestCase):
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

    def test_inputs_none(self):
        """No inputs are given"""
        self.assertEquals(Visualization().backtest_report, None)
        self.assertEquals(Visualization().height, -1)
        self.assertEquals(Visualization().width, -1)

    def test_all_inputs(self):
        """All inputs given as input"""
        self.assertEquals(Visualization(backtest_report=BackTestReport.objects.all()[0]).backtest_report, BackTestReport.objects.all()[0])
        self.assertEquals(Visualization(height=5).height, 5)
        self.assertEquals(Visualization(width=5).width, 5)

    def test_get_visualization_errors(self):
        """Checks if errors are raised if invalid inputs are given"""
        self.assertRaises(ValueError, Visualization(backtest_report=BackTestReport.objects.all()[0], height=0,
                                                    width=5).get_visualization)
        self.assertRaises(ValueError, Visualization(backtest_report=BackTestReport.objects.all()[0], height=5,
                                                    width=0).get_visualization)
        self.assertRaises(ValueError, Visualization(backtest_report=BackTestReport.objects.all()[0], height=-7,
                                                    width=5).get_visualization)
        self.assertRaises(ValueError, Visualization(backtest_report=BackTestReport.objects.all()[0], height=5,
                                                    width=-7).get_visualization)
        self.assertRaises(ValueError, Visualization(backtest_report="abc", height=5,
                                                    width=5).get_visualization)

    def test_get_visualization_correct(self):
        """Checks if the generate_backtest_report method works correctly"""
        self.assertEquals(Visualization(backtest_report=BackTestReport.objects.all()[0], height=5,
                                        width=5).get_visualization(), None)
