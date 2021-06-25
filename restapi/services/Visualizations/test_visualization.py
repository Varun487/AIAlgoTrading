import pandas as pd
from django.test import TestCase

from .visualization import Visualization


class VisualizationTestCase(TestCase):
    def setUp(self) -> None:
        # create dataframe for input
        self.df = pd.read_csv('/home/app/restapi/services/TCS_Yahoo_data.csv')
        self.df.drop(['Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)
        self.df['time_stamp'] = [time_stamp + " 00:00:00+00:00" for time_stamp in self.df['time_stamp']]

    def test_inputs_none(self):
        """No inputs are given"""
        self.assertEquals(Visualization().df, None)
        self.assertEquals(Visualization().columns, None)
        self.assertEquals(Visualization().height, -1)
        self.assertEquals(Visualization().width, -1)

    def test_all_inputs(self):
        """All inputs given as input"""
        self.assertEquals(Visualization(df=self.df).df.equals(self.df), True)
        self.assertEquals(Visualization(columns=["a", "b", "c"]).columns, ["a", "b", "c"])
        self.assertEquals(Visualization(height=5).height, 5)
        self.assertEquals(Visualization(width=5).width, 5)

    def test_get_visualization_errors(self):
        """Checks if errors are raised if invalid inputs are given"""
        self.assertRaises(ValueError, Visualization(df="abc", columns=['close', 'open', 'high', 'low', 'volume',
                                                                       'time_stamp'], height=5,
                                                    width=5).get_visualization)
        self.assertRaises(ValueError, Visualization(df=self.df, columns=['open', 'high', 'low', 'volume',
                                                                         'time_stamp'], height=5,
                                                    width=5).get_visualization)
        self.assertRaises(ValueError, Visualization(df=self.df, columns="abc", height=5, width=5).get_visualization)
        self.assertRaises(ValueError, Visualization(df=self.df, columns=['close', 'open', 'high', 'low', 'volume',
                                                                         'time_stamp'], height=-3,
                                                    width=5).get_visualization)
        self.assertRaises(ValueError, Visualization(df=self.df, columns=['close', 'open', 'high', 'low', 'volume',
                                                                         'time_stamp'], height=5,
                                                    width=-1).get_visualization)
        self.assertRaises(ValueError, Visualization(df=self.df, columns=['close', 'open', 'high', 'low', 'volume',
                                                                         'time_stamp'], height=0,
                                                    width=5).get_visualization)
        self.assertRaises(ValueError, Visualization(df=self.df, columns=['close', 'open', 'high', 'low', 'volume',
                                                                         'time_stamp'], height=5,
                                                    width=0).get_visualization)

    def test_get_visualization_correct(self):
        """Checks if the generate_backtest_report method works correctly"""
        self.assertEquals(Visualization(df=self.df, columns=['close', 'open', 'high', 'low', 'volume', 'time_stamp'],
                                        height=5, width=5).get_visualization(), None)
