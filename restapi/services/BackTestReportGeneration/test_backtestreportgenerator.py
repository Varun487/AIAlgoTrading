from django.test import TestCase
import pandas as pd

from services.TradeEvaluation.tradeevaluator import TradeEvaluator
from services.OrderExecution.orderexecution import OrderExecution
from services.IndicatorCalc.indicators import BollingerIndicator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator

from .backtestreportgenerator import BackTestReportGenerator


class BackTestReportGeneratorTestCase(TestCase):
    def setUp(self) -> None:
        # create dataframe
        self.df = pd.read_csv('/home/app/restapi/services/TCS_Yahoo_data.csv')
        self.df.drop(['Volume', 'Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low'}, inplace=True)

        # # generate signals
        # self.signals_df = BBSignalGenerator(
        #     indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1)
        # ).generate_signals()
        #
        # # calc take profit and stop loss
        # self.tp_sl_df = TakeProfitAndStopLossBB(df=self.signals_df, dimension="close", factor=1).get_calc_df()
        #
        # # Execute orders
        # self.orders_df = OrderExecution(df=self.tp_sl_df, max_holding_period=3, dimension="close").execute()
        #
        # # Evaluate trades
        # self.eval_trades_df = TradeEvaluator(df=self.orders_df).get_evaluated_df()

    def test_inputs_none(self):
        """No inputs are given"""
        self.assertEquals(BackTestReportGenerator().df, None)
        self.assertEquals(BackTestReportGenerator().time_period, -1)
        self.assertEquals(BackTestReportGenerator().dimension, None)
        self.assertEquals(BackTestReportGenerator().sigma, -1)
        self.assertEquals(BackTestReportGenerator().factor, -1)
        self.assertEquals(BackTestReportGenerator().max_holding_period, -1)

        self.assertEquals(BackTestReportGenerator().indicator, None)
        self.assertEquals(BackTestReportGenerator().signal_generator, None)
        self.assertEquals(BackTestReportGenerator().take_profit_stop_loss, None)
        self.assertEquals(BackTestReportGenerator().order_executor, None)
        self.assertEquals(BackTestReportGenerator().trade_evaluator, None)

    def test_all_inputs(self):
        """All inputs given as input"""
        self.assertEquals(BackTestReportGenerator(df=self.df).df.equals(self.df), True)
        self.assertEquals(BackTestReportGenerator(time_period=5).time_period, 5)
        self.assertEquals(BackTestReportGenerator(dimension="close").dimension, "close")
        self.assertEquals(BackTestReportGenerator(sigma=1).sigma, 1)
        self.assertEquals(BackTestReportGenerator(factor=1).factor, 1)
        self.assertEquals(BackTestReportGenerator(max_holding_period=5).max_holding_period, 5)

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

    def test_generate_backtest_report_correct(self):
        """Checks if the generate_backtest_report method works correctly"""
        BackTestReportGenerator(df=self.df, time_period=5, dimension="close", sigma=1, factor=1, max_holding_period=5,
                                indicator=BollingerIndicator, signal_generator=BBSignalGenerator,
                                take_profit_stop_loss=TakeProfitAndStopLossBB, order_executor=OrderExecution,
                                trade_evaluator=TradeEvaluator).generate_backtest_report()
