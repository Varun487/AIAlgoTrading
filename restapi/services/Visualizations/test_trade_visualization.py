import pandas as pd
from django.test import TestCase

from .trade_visualization import TradeVisualization
from services.IndicatorCalc.indicators import BollingerIndicator
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.OrderExecution.orderexecution import OrderExecution

from services.TradeEvaluation.tradeevaluator import TradeEvaluator


class TradeVisualizationTestCase(TestCase):
    def setUp(self) -> None:
        # create dataframe for input
        self.df = pd.read_csv('/home/app/restapi/services/TCS_Yahoo_data.csv')
        self.df.drop(['Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)
        self.df['time_stamp'] = [time_stamp + " 00:00:00+00:00" for time_stamp in self.df['time_stamp']]

        self.signals_df = BBSignalGenerator(
            indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1)
        ).generate_signals()

        self.tp_sl_df = TakeProfitAndStopLossBB(df=self.signals_df, dimension="close", factor=1).get_calc_df()

        # Execute orders
        self.orders_df = OrderExecution(df=self.tp_sl_df, max_holding_period=5, dimension="close").execute()

        # Evaluate trades
        self.trades_df = TradeEvaluator(df=self.orders_df).get_evaluated_df()

    def test_generate_visualization_errors(self):
        """Checks if the generate_visualization method works correctly"""
        self.assertRaises(ValueError, TradeVisualization(df=self.trades_df, columns=self.signals_df.columns, height=6,
                                                         width=15).generate_visualization)
        self.assertRaises(ValueError, TradeVisualization(df=self.trades_df, columns=self.signals_df.columns, height=6,
                                                         width=15, trade_number=0).generate_visualization)
        self.assertRaises(ValueError, TradeVisualization(df=self.trades_df, columns=self.signals_df.columns, height=6,
                                                         width=15, trade_number=-3).generate_visualization)

    def test_generate_visualization(self):
        """Checks if the generate_visualization method works correctly"""
        TradeVisualization(df=self.trades_df, columns=self.signals_df.columns, height=6,
                           width=15, trade_number=7).generate_visualization()
