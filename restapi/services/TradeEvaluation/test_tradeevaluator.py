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
        self.orders_df = OrderExecution(df=self.tp_sl_df, max_holding_period=5, dimension="close").execute()

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(TradeEvaluator().df, None)

    def test_input_df(self):
        """DF is given as input"""
        self.assertEquals(TradeEvaluator(df=self.orders_df).df.equals(self.orders_df), True)

    def test_get_evaluated_df_errors(self):
        """Checks if errors are raised if invalid inputs are given"""
        self.assertRaises(ValueError, TradeEvaluator(df="abc").get_evaluated_df)

    def test_get_evaluated_df_correct(self):
        """Checks if the get_evaluated_df method works correctly"""
        TradeEvaluator(df=self.orders_df).get_evaluated_df()
