import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import warnings
warnings.filterwarnings("ignore")

from django.test import TestCase
import pandas as pd

# from services.IndicatorCalc.indicators import BollingerIndicator
# from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
# from .calctakeprofitstoploss import CalcTakeProfitStopLoss, TakeProfitAndStopLossBB
from ta import add_all_ta_features

from .predictions import Predictions

from strategies.models import Company


class PredictionsTestCase(TestCase):

    def setUp(self) -> None:
        # create a company
        Company(name="ONGC", ticker="ONGC.NS", description="No description").save()

        # create dataframe for input
        self.df = pd.read_csv('/home/app/restapi/services/ModelPredictions/Storage/CompanyData/ONGC.NS.csv')

        self.df = add_all_ta_features(self.df, open="open", high="high", low="low", close="close",
                                      volume="volume", fillna=True)

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(Predictions().ticker, None)
        self.assertEquals(Predictions().period, None)
        self.assertEquals(Predictions().split_factor, None)
        self.assertEquals(Predictions().epochs, None)
        self.assertEquals(Predictions().df, None)

    def test_all_inputs(self):
        """All inputs are given"""
        p = Predictions(df=self.df, ticker="ONGC.NS", period=2, split_factor=0.8, epochs=10)
        self.assertEquals(p.ticker, "ONGC.NS")
        self.assertEquals(p.period, 2)
        self.assertEquals(p.split_factor, 0.8)
        self.assertEquals(p.epochs, 10)
        self.assertEquals(p.df.equals(self.df), True)

    def test_get_prediction_errors(self):
        """Tests get_predictions method"""
        # Invalid period
        self.assertRaises(ValueError, Predictions(df=self.df, ticker="ONGC.NS", period=-1, split_factor=0.8, epochs=10)
                          .get_prediction)
        self.assertRaises(ValueError, Predictions(df=self.df, ticker="ONGC.NS", period=0, split_factor=0.8, epochs=10)
                          .get_prediction)

        # Invalid epochs
        self.assertRaises(ValueError, Predictions(df=self.df, ticker="ONGC.NS", period=2, split_factor=0.8, epochs=-1)
                          .get_prediction)
        self.assertRaises(ValueError, Predictions(df=self.df, ticker="ONGC.NS", period=2, split_factor=0.8, epochs=0)
                          .get_prediction)

        # Invalid split factor
        self.assertRaises(ValueError, Predictions(df=self.df, ticker="ONGC.NS", period=2, split_factor=0, epochs=10)
                          .get_prediction)
        self.assertRaises(ValueError, Predictions(df=self.df, ticker="ONGC.NS", period=2, split_factor=1, epochs=10)
                          .get_prediction)
        self.assertRaises(ValueError, Predictions(df=self.df, ticker="ONGC.NS", period=2, split_factor=-3, epochs=10)
                          .get_prediction)
        self.assertRaises(ValueError, Predictions(df=self.df, ticker="ONGC.NS", period=2, split_factor=7, epochs=10)
                          .get_prediction)

        # Invalid tickers
        self.assertRaises(ValueError, Predictions(df=self.df, ticker=9, period=2, split_factor=0.8, epochs=10)
                          .get_prediction)
        self.assertRaises(ValueError, Predictions(df=self.df, ticker="ABCD.NS", period=2, split_factor=0.8, epochs=10)
                          .get_prediction)

        # Invalid dataframe
        self.assertRaises(ValueError, Predictions(df="abc", ticker="ONGC.NS", period=2, split_factor=0.8, epochs=10)
                          .get_prediction)
        self.assertRaises(ValueError, Predictions(df=5, ticker="ONGC.NS", period=2, split_factor=0.8, epochs=10)
                          .get_prediction)
        self.assertRaises(ValueError, Predictions(df=pd.DataFrame(), ticker="ONGC.NS", period=0.8, split_factor=0, epochs=10)
                          .get_prediction)
        self.assertRaises(ValueError, Predictions(ticker="ONGC.NS", period=2, split_factor=0.8, epochs=10)
                          .get_prediction)

    # def test_get_prediction(self):
    #     Predictions(df=self.df, ticker="ONGC.NS", period=2, split_factor=0.8, epochs=10).get_prediction()
