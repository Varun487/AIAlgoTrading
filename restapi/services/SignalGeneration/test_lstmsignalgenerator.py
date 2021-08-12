from django.test import TestCase

import pandas as pd

from .lstmsignalgenerator import LSTMSignalGenerator
from services.IndicatorCalc.indicators import AllIndicators

from strategies.models import StrategyType, StrategyConfig, Company

from services.BackTestReportGeneration.backtestreportgenerator import BackTestReportGenerator

from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.OrderExecution.orderexecution import OrderExecution
from services.TradeEvaluation.tradeevaluator import TradeEvaluator

from backtester.models import BackTestReport

from services.Utils.pusher import Pusher
from strategies.models import TickerData


class LSTMSignalGeneratorTestCase(TestCase):

    def setUp(self) -> None:
        # Create dataframe for input
        self.df = pd.read_csv('/home/app/restapi/services/ModelPredictions/Storage/CompanyData/TCS.NS.csv')
        # self.df.drop(['Adj Close'], axis=1, inplace=True)
        self.df.rename(columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                                'Volume': 'volume'},
                       inplace=True)
        # self.df['time_stamp'] = [time_stamp + " 00:00:00+05:30" for time_stamp in self.df['time_stamp']]

        c = Company(
            name='TCS',
            ticker='TCS.NS',
            description='BRUH',
        )

        c.save()

        self.push_df = self.df.copy()
        self.push_df.drop(['Adj Close'], axis=1, inplace=True)
        self.push_df['time_period'] = "1"
        self.push_df['company'] = Company.objects.all()[0]

        Pusher(df=self.push_df).push(TickerData)

        st = StrategyType(
            name='LSTM TCS',
            description='example',
            stock_selection='TCS',
            entry_criteria='Bruh',
            exit_criteria='Bruh',
            stop_loss_method='example',
            take_profit_method='example'
        )

        st.save()

        StrategyConfig(
            strategy_type=st,
            indicator_time_period=20,
            max_holding_period=20,
            take_profit_factor=1,
            stop_loss_factor=1,
            sigma=1,
            lstm_buy_threshold=0.01,
            lstm_sell_threshold=-0.1,
            lstm_model_time_period=2,
            lstm_company=c,
        ).save()

    def test_generate_signals(self):
        """Check if correct signals are generated"""
        signals_df = LSTMSignalGenerator(
            indicator=AllIndicators(df=self.df, time_period=5, dimension="close", sigma=1),
            strategy_config=StrategyConfig.objects.all()[0],
        ).generate_signals()

        assert 'SIGNAL' in signals_df.columns

    def test_backtest(self):
        """Run a test backtest of the strategy"""
        btr = BackTestReportGenerator(
            df=self.df,
            ticker_time_period='1',
            indicator_time_period=20,
            dimension="close",
            sigma=1,
            factor=1,
            max_holding_period=20,
            company=Company.objects.all()[0],
            strategy_type=StrategyType.objects.all()[0],
            indicator=AllIndicators,
            strategy_config=StrategyConfig.objects.all()[0],
            signal_generator=LSTMSignalGenerator,
            take_profit_stop_loss=TakeProfitAndStopLossBB,
            order_executor=OrderExecution,
            trade_evaluator=TradeEvaluator,
        )

        btr.generate_backtest_report()

        assert len(BackTestReport.objects.all()) == 1
