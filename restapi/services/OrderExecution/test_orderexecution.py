from django.test import TestCase
import pandas as pd

from services.IndicatorCalc.indicators import BollingerIndicator
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from .calctakeprofitstoploss import TakeProfitAndStopLossBB
from .orderexecution import OrderExecution


class OrderExecutionTestCase(TestCase):

    def setUp(self) -> None:
        self.df = pd.DataFrame()
        self.df["close"] = [3114.00, 3158.50, 3180.00, 3143.60, 3159.15, 3153.00, 3129.45, 3141.25, 3143.75, 3183.20,
                            3200.15]

        self.signals_df = BBSignalGenerator(
            indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1)
        ).generate_signals()

        self.tp_sl_df = TakeProfitAndStopLossBB(df=self.signals_df, dimension="close", factor=1).get_calc_df()

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(OrderExecution().df, None)
        self.assertEquals(OrderExecution().max_holding_period, -1)
        self.assertEquals(OrderExecution().dimension, None)

    def test_input_df(self):
        """Only DF is given as input"""
        self.assertEquals(OrderExecution(df=self.tp_sl_df).df.equals(self.tp_sl_df), True)
        self.assertEquals(OrderExecution(df=self.tp_sl_df).max_holding_period, -1)
        self.assertEquals(OrderExecution(df=self.tp_sl_df).dimension, None)

    def test_input_max_holding_period(self):
        """Only Max holding is given"""
        self.assertEquals(OrderExecution(max_holding_period=20).df, None)
        self.assertEquals(OrderExecution(max_holding_period=20).max_holding_period, 20)
        self.assertEquals(OrderExecution(max_holding_period=20).dimension, None)

    def test_input_dimension(self):
        """Only Dimension is given"""
        self.assertEquals(OrderExecution(dimension="close").dimension, "close")
        self.assertEquals(OrderExecution(dimension="close").df, None)
        self.assertEquals(OrderExecution(dimension="close").max_holding_period, -1)

    def test_all_inputs(self):
        """All inputs are given"""
        self.assertEquals(OrderExecution(df=self.tp_sl_df, max_holding_period=20, dimension="close").df.equals(self.tp_sl_df), True)
        self.assertEquals(OrderExecution(df=self.tp_sl_df, max_holding_period=20, dimension="close").max_holding_period, 20)
        self.assertEquals(OrderExecution(df=self.tp_sl_df, max_holding_period=20, dimension="close").dimension, "close")

    def test_execute_errors(self):
        """Tests if execute method validates"""
        # raises errors if input is not valid
        self.assertRaises(ValueError, OrderExecution(df=self.tp_sl_df, max_holding_period=-1,dimension="close").execute)
        self.assertRaises(ValueError, OrderExecution(df=self.tp_sl_df, max_holding_period=0,dimension="close").execute)
        self.assertRaises(ValueError, OrderExecution(df="abc", max_holding_period=20,dimension="close").execute)
        self.assertRaises(ValueError, OrderExecution(df="abc", max_holding_period=-20,dimension="close").execute)
        self.assertRaises(ValueError, OrderExecution(df=self.tp_sl_df, max_holding_period=20,dimension="closss").execute)

    def test_execute_correct(self):
        """Tests if execute method validates"""
        OrderExecution(df=self.tp_sl_df, max_holding_period=2, dimension="close").execute()
        # print(self.tp_sl_df)
