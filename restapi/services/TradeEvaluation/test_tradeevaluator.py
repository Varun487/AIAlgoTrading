from django.test import TestCase
import pandas as pd

from .tradeevaluator import TradeEvaluator

from services.OrderExecution.orderexecution import OrderExecution
from services.IndicatorCalc.indicators import BollingerIndicator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator


class TradeEvaluatorTestCase(TestCase):
    def setUp(self) -> None:
        # create dataframe
        self.df = pd.read_csv('/home/app/restapi/services/TCS_Yahoo_data.csv')
        self.df.rename(columns={'Close': 'close'}, inplace=True)

        # generate signals
        self.signals_df = BBSignalGenerator(
            indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1)
        ).generate_signals()

        # calc take profit and stop loss
        self.tp_sl_df = TakeProfitAndStopLossBB(df=self.signals_df, dimension="close", factor=1).get_calc_df()

        # Execute orders
        self.orders_df = OrderExecution(df=self.tp_sl_df, max_holding_period=2, dimension="close").execute()

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(TradeEvaluator().df, None)
        self.assertEquals(TradeEvaluator().dimension, None)

    def test_input_df(self):
        """Only DF is given as input"""
        self.assertEquals(TradeEvaluator(df=self.orders_df).df.equals(self.orders_df), True)
        self.assertEquals(TradeEvaluator(df=self.orders_df).dimension, None)

    def test_input_dimension(self):
        """Only Dimension is given"""
        self.assertEquals(TradeEvaluator(dimension="close").dimension, "close")
        self.assertEquals(TradeEvaluator(dimension="close").df, None)

    def test_all_inputs(self):
        """All inputs are given"""
        self.assertEquals(TradeEvaluator(df=self.orders_df, dimension="close").df.equals(self.orders_df), True)
        self.assertEquals(TradeEvaluator(df=self.orders_df, dimension="close").dimension, "close")

    def test_get_evaluated_df_errors(self):
        """Checks if errors are raised if invalid inputs are given"""
        self.assertRaises(ValueError, TradeEvaluator(df=self.orders_df, dimension="clos").get_evaluated_df)
        self.assertRaises(ValueError, TradeEvaluator(df="abc", dimension="close").get_evaluated_df)

    def test_get_evaluated_df_correct(self):
        """Checks if the get_evaluated_df method works correctly"""
        TradeEvaluator(df=self.orders_df, dimension="close").get_evaluated_df()
