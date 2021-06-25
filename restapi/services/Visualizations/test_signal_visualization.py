import pandas as pd
from django.test import TestCase

from .signal_visualization import SignalVisualization
from services.IndicatorCalc.indicators import BollingerIndicator
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator


class VisualizationTestCase(TestCase):
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

    def test_generate_visualization(self):
        """Checks if the generate_visualization method works correctly"""
        SignalVisualization(df=self.signals_df, columns=self.signals_df.columns, height=6,
                            width=15).generate_visualization()
