from django.test import TestCase
import pandas as pd

from strategies.models import Company
from strategies.models import TickerData
from strategies.models import StrategyType
from strategies.models import StrategyConfig
from strategies.models import Signal
from strategies.models import Order
from strategies.models import Trade


from services.Utils.pusher import Pusher
from services.TradeEvaluation.tradeevaluator import TradeEvaluator
from services.OrderExecution.orderexecution import OrderExecution
from services.IndicatorCalc.indicators import BollingerIndicator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator

from .backtestreportgenerator import BackTestReportGenerator


class BackTestReportGeneratorTestCase(TestCase):
    def setUp(self) -> None:
        # create dataframe for input
        self.df = pd.read_csv('/home/app/restapi/services/TCS_Yahoo_data.csv')
        self.df.drop(['Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)
        self.df['time_stamp'] = [time_stamp+" 00:00:00+00:00" for time_stamp in self.df['time_stamp']]

        # push dummy company to db
        Company(name="TCS", ticker="TCS.NS", description="Test company").save()

        # push Dummy company data to db
        self.company_df = self.df.copy()
        self.company_df['time_period'] = "1"
        self.company_df['company'] = Company.objects.all()[0]

        Pusher(df=self.company_df).push(TickerData)

        st = StrategyType(name="Test", description="Test", stock_selection="Test", entry_criteria="Test",
                          exit_criteria="Test", stop_loss_method="Test", take_profit_method="Test")
        st.save()

        sc = StrategyConfig(strategy_type=st, indicator_time_period=5, max_holding_period=2, take_profit_factor=1,
                            stop_loss_factor=1, sigma=1, dimension="1")
        sc.save()

    def test_inputs_none(self):
        """No inputs are given"""
        self.assertEquals(BackTestReportGenerator().df, None)
        self.assertEquals(BackTestReportGenerator().ticker_time_period, -1)
        self.assertEquals(BackTestReportGenerator().indicator_time_period, -1)
        self.assertEquals(BackTestReportGenerator().dimension, None)
        self.assertEquals(BackTestReportGenerator().sigma, -1)
        self.assertEquals(BackTestReportGenerator().factor, -1)
        self.assertEquals(BackTestReportGenerator().max_holding_period, -1)

        self.assertEquals(BackTestReportGenerator().company, None)
        self.assertEquals(BackTestReportGenerator().strategy_config, None)
        self.assertEquals(BackTestReportGenerator().strategy_type, None)
        self.assertEquals(BackTestReportGenerator().indicator, None)
        self.assertEquals(BackTestReportGenerator().signal_generator, None)
        self.assertEquals(BackTestReportGenerator().take_profit_stop_loss, None)
        self.assertEquals(BackTestReportGenerator().order_executor, None)
        self.assertEquals(BackTestReportGenerator().trade_evaluator, None)

    def test_all_inputs(self):
        """All inputs given as input"""
        self.assertEquals(BackTestReportGenerator(df=self.df).df.equals(self.df), True)
        self.assertEquals(BackTestReportGenerator(ticker_time_period=5).ticker_time_period, 5)
        self.assertEquals(BackTestReportGenerator(indicator_time_period=5).indicator_time_period, 5)
        self.assertEquals(BackTestReportGenerator(dimension="close").dimension, "close")
        self.assertEquals(BackTestReportGenerator(sigma=1).sigma, 1)
        self.assertEquals(BackTestReportGenerator(factor=1).factor, 1)
        self.assertEquals(BackTestReportGenerator(max_holding_period=5).max_holding_period, 5)

        self.assertEquals(BackTestReportGenerator(company=Company).company, Company)
        self.assertEquals(BackTestReportGenerator(strategy_type=StrategyType).strategy_type, StrategyType)
        self.assertEquals(BackTestReportGenerator(strategy_config=StrategyConfig).strategy_config, StrategyConfig)
        self.assertEquals(BackTestReportGenerator(indicator=BollingerIndicator).indicator, BollingerIndicator)
        self.assertEquals(BackTestReportGenerator(signal_generator=BBSignalGenerator).signal_generator,
                          BBSignalGenerator)
        self.assertEquals(BackTestReportGenerator(take_profit_stop_loss=TakeProfitAndStopLossBB).take_profit_stop_loss,
                          TakeProfitAndStopLossBB)
        self.assertEquals(BackTestReportGenerator(order_executor=OrderExecution).order_executor, OrderExecution)
        self.assertEquals(BackTestReportGenerator(trade_evaluator=TradeEvaluator).trade_evaluator, TradeEvaluator)

    def test_generate_backtest_report_errors(self):
        """Checks if errors are raised if invalid inputs are given"""
        self.assertRaises(ValueError, BackTestReportGenerator(df="abc").generate_backtest_report)
        self.assertRaises(ValueError, BackTestReportGenerator(company="abc").generate_backtest_report)
        self.assertRaises(ValueError, BackTestReportGenerator(strategy_type="abc").generate_backtest_report)
        self.assertRaises(ValueError, BackTestReportGenerator(strategy_config="abc").generate_backtest_report)
        self.assertRaises(ValueError, BackTestReportGenerator(indicator="abc").generate_backtest_report)
        self.assertRaises(ValueError, BackTestReportGenerator(signal_generator="abc").generate_backtest_report)
        self.assertRaises(ValueError, BackTestReportGenerator(take_profit_stop_loss="abc").generate_backtest_report)
        self.assertRaises(ValueError, BackTestReportGenerator(order_executor="abc").generate_backtest_report)
        self.assertRaises(ValueError, BackTestReportGenerator(trade_evaluator="abc").generate_backtest_report)

    def test_generate_backtest_report_correct(self):
        """Checks if the generate_backtest_report method works correctly"""
        BackTestReportGenerator(df=self.df, ticker_time_period="1", indicator_time_period=5, dimension="close", sigma=1,
                                factor=1, max_holding_period=5, company=Company.objects.get(id=2),
                                strategy_config=StrategyConfig.objects.get(id=2),
                                strategy_type=StrategyType.objects.get(id=2),
                                indicator=BollingerIndicator, signal_generator=BBSignalGenerator,
                                take_profit_stop_loss=TakeProfitAndStopLossBB, order_executor=OrderExecution,
                                trade_evaluator=TradeEvaluator).generate_backtest_report()
