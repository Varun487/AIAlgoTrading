from django.test import TestCase
import pandas as pd

from services.IndicatorCalc.indicators import BollingerIndicator
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from .calctakeprofitstoploss import CalcTakeProfitStopLoss, TakeProfitAndStopLossBB


class CalcTakeProfitSTopLoss(TestCase):

    def setUp(self) -> None:
        self.df = pd.DataFrame()
        self.df["close"] = [3114.00, 3158.50, 3180.00, 3143.60, 3159.15, 3153.00, 3129.45, 3141.25, 3143.75, 3183.20,
                            3200.15]

        self.signals_df = BBSignalGenerator(
            indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1)
        ).generate_signals()

    def test_input_none(self):
        """No inputs are given"""
        self.assertEquals(CalcTakeProfitStopLoss().df, None)
        self.assertEquals(CalcTakeProfitStopLoss().factor, -1)

    def test_input_df(self):
        """Only DF is given as input"""
        self.assertEquals(CalcTakeProfitStopLoss(df=self.df).df.equals(self.df), True)
        self.assertEquals(CalcTakeProfitStopLoss(df=self.df).factor, -1)

    def test_input_factor(self):
        """Only factor is given as input"""
        self.assertEquals(CalcTakeProfitStopLoss(factor=2).df, None)
        self.assertEquals(CalcTakeProfitStopLoss(factor=2).factor, 2)

    def test_all_inputs(self):
        """All inputs are given"""
        self.assertEquals(CalcTakeProfitStopLoss(df=self.df, factor=2).df.equals(self.df), True)
        self.assertEquals(CalcTakeProfitStopLoss(df=self.df, factor=2).factor, 2)

    def test_get_calc_df(self):
        """Tests get_calc_df method"""
        # check validation
        self.assertRaises(ValueError, CalcTakeProfitStopLoss(df=self.signals_df, factor=0).get_calc_df)
        self.assertRaises(ValueError, CalcTakeProfitStopLoss(df=self.signals_df, factor=-1).get_calc_df)
        self.assertRaises(ValueError, CalcTakeProfitStopLoss(df=self.signals_df, factor=-3).get_calc_df)
        self.assertRaises(ValueError, CalcTakeProfitStopLoss(df="abc", factor=2).get_calc_df)
        self.assertRaises(ValueError, CalcTakeProfitStopLoss(factor=2).get_calc_df)
        self.assertRaises(ValueError, CalcTakeProfitStopLoss(df=self.signals_df).get_calc_df)

        # check if correct output is given
        self.assertEquals(CalcTakeProfitStopLoss(df=self.signals_df, factor=2).get_calc_df().equals(self.signals_df),
                          True)


class TakeProfitAndStopLossBBTestCase(TestCase):

    def setUp(self) -> None:
        self.df = pd.DataFrame()
        self.df["close"] = [3114.00, 3158.50, 3180.00, 3143.60, 3159.15, 3153.00, 3129.45, 3141.25, 3143.75, 3183.20,
                            3200.15]

        self.signals_df = BBSignalGenerator(
            indicator=BollingerIndicator(df=self.df, time_period=5, dimension="close", sigma=1)
        ).generate_signals()

        self.temp_df = self.signals_df.copy()
        self.take_profit = [-1]
        self.stop_loss = [-1]

        for i in range(1, len(self.temp_df)):
            if self.temp_df["SIGNAL"][i] != "FLAT" and i != 0:

                # Absolute difference of the prev close price and current close price * factor
                risk = abs(self.temp_df["close"][i] - self.temp_df["close"][i - 1]) * 1
                dimension_plus_risk = self.temp_df["close"][i] + risk
                dimension_minus_risk = self.temp_df["close"][i] - risk

                if self.temp_df['SIGNAL'][i] == 'BUY':
                    self.take_profit.append(dimension_plus_risk)
                    self.stop_loss.append(dimension_minus_risk)
                else:
                    self.take_profit.append(dimension_minus_risk)
                    self.stop_loss.append(dimension_plus_risk)

            else:
                self.take_profit.append(-1)
                self.stop_loss.append(-1)

        self.temp_df["takeprofit"] = self.take_profit
        self.temp_df["stoploss"] = self.stop_loss


    def test_input_dimension(self):
        """Checks if dimension input behaves correctly"""
        self.assertEquals(TakeProfitAndStopLossBB(df=self.signals_df, factor=2, dimension="close").dimension, "close")
        self.assertEquals(TakeProfitAndStopLossBB(df=self.signals_df, factor=2).dimension, None)

    def test_validate_dimension(self):
        """Checks if dimension is validated correctly"""
        test1 = TakeProfitAndStopLossBB(df=self.signals_df, factor=2, dimension="close")
        test1.validate_dimension()
        self.assertEquals(test1.valid_dimension, True)

        test2 = TakeProfitAndStopLossBB(df=self.signals_df, factor=2, dimension="clos")
        test2.validate_dimension()
        self.assertEquals(test2.valid_dimension, False)

    def test_generate_prices(self):
        """Tests price generation method"""
        self.assertEquals(TakeProfitAndStopLossBB(df=self.signals_df, factor=1, dimension="close").get_calc_df().equals
                          (self.temp_df), True)
