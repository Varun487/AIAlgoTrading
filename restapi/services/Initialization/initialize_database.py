import time

# Get all services required
from services.IndicatorCalc.indicators import BollingerIndicator
from services.Initialization.add_companies import AddCompanies
from services.Initialization.add_companies_data import AddCompaniesData
from services.Initialization.add_db_object import AddDBObject
from services.Initialization.automated_backtests import AutomatedBacktests
from services.Initialization.clean_database import CleanDatabase
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.OrderExecution.orderexecution import OrderExecution
from services.PaperTradeSynchronizer.papertradesynchronizer import PaperTradeSynchronizer
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from services.TradeEvaluation.tradeevaluator import TradeEvaluator

# Get all models required
from strategies.models import Company
from strategies.models import ExampleStrategiesModel
from strategies.models import IndicatorType
from strategies.models import StrategyConfig
from strategies.models import StrategyType
from strategies.models import VisualizationType

from django.contrib.auth.models import User

from backtester.models import ExampleBackTesterModel

from papertrader.models import ExamplePaperTraderModel
from papertrader.models import PaperTradedStrategy

# EXAMPLE STRATEGIES DATA
example_strategies_data = {
    'name': [
        'hello-strategies'
    ]
}

# INDICATOR TYPES DATA
indicator_types_data = {
    'name': [
        'Bollinger Bands Indicator',
        'All Indicators',
    ],
    'description': [
        'The indicator is used for the Simple Bollinger bands strategy. Calculates the Simple Moving Average and n '
        'standard deviations above and below the simple moving average',
        'The indicator is used for the LSTM strategy. Calculates all indicators provided by ta module with default '
        'values',
    ]
}

# STRATEGY TYPES DATA
strategy_types_data = {
    'name': [
        'Simple Bollinger Band Strategy',
        'LSTM Strategy',
    ],
    'description': [
        'This strategy uses the Bollinger Bands indicator to generate signals.',
        'This strategy uses the predictions from a custom built LSTM model to generate signals.',
    ],
    'stock_selection': [
        'All Stocks / Crypto / Forex / Commodities applicable.',
        'Only NIFTY 50 Stocks applicable.',
    ],
    'entry_criteria': [
        'BUY signal if stock price < n std. dev below SMA. SELL signal if stock price > n std. dev above SMA.',
        'BUY signal if the predicted price percentage increase > BUY threshold. '
        'SELL signal if the if the predicted price percentage decrease < SELL threshold.',
    ],
    'exit_criteria': [
        'If stock held for the max holding period or price crosses take profit or stop loss limits.',
        'If stock held for the max holding period or price crosses take profit or stop loss limits.',
    ],
    'stop_loss_method': [
        '((close price of previous candlestick - current close price) * factor) is added or subtracted from current '
        'close price',
        '((close price of previous candlestick - current close price) * factor) is added or subtracted from current '
        'close price',
    ],
    'take_profit_method': [
        '((close price of previous candlestick - current close price) * factor) is added or subtracted from current '
        'close price',
        '((close price of previous candlestick - current close price) * factor) is added or subtracted from current '
        'close price',
    ],
}

# BB STRATEGY CONFIGS DATA
bb_strategy_configs_data = {
    'indicator_time_period': [item for sublist in
                              [[5 for i in range(5)] +
                               [10 for i in range(5)] +
                               [15 for i in range(5)] +
                               [25 for i in range(5)]]
                              for item in sublist],
    'max_holding_period': [item for sublist in [[5, 7, 10, 14, 21] for i in range(4)] for item in sublist],
    'take_profit_factor': [item for sublist in [[1, 2] for i in range(10)] for item in sublist],
    'stop_loss_factor': [item for sublist in [[1, 2] for i in range(10)] for item in sublist],
    'sigma': [item for sublist in [[1, 2] for i in range(10)] for item in sublist],
    'dimension': [item for sublist in [[1, 2, 3, 4] for i in range(5)] for item in sublist],
    'lstm_buy_threshold': [0 for i in range(20)],
    'lstm_sell_threshold': [0 for i in range(20)],
    'lstm_model_time_period': [0 for i in range(20)],
}

# LSTM STRATEGY CONFIGS DATA
lstm_strategy_configs_data = {
    'indicator_time_period': [item for sublist in
                              [[5, 7, 10, 15, 25] for i in range(500)]
                              for item in sublist],
    'max_holding_period': [item for sublist in [[2, 3, 5, 7, 10, 12, 15, 17, 20, 21] for i in range(250)] for item in
                           sublist],
    'take_profit_factor': [item for sublist in [[1, 2] for i in range(1250)] for item in sublist],
    'stop_loss_factor': [item for sublist in [[2, 1, 1, 2] for i in range(625)] for item in sublist],
    'sigma': [item for sublist in [[1, 2, 2, 1] for i in range(625)] for item in sublist],
    'dimension': [item for sublist in [[1, 2, 3, 4] for i in range(625)] for item in sublist],
    'lstm_buy_threshold': [item for sublist in
                           [[0.01, 0.015, 0.03, 0.08, 0.1, 0.15, 0.08, 0.02, 0.2, 1.0,
                             0.07, 0.06, 0.05, 0.09, 0.2, 0.3, 0.5, 0.17, 0.25, 0.19]
                            for i in range(125)]
                           for item in sublist],
    'lstm_sell_threshold': [item for sublist in
                            [[-0.013, -0.015, -0.035, -0.085, -0.1, -0.15, -0.08, -0.02, -0.2, -1.0,
                              -0.06, -0.065, -0.05, -0.023, -0.2, -0.3, -0.5, -0.17, -0.25, -0.19]
                             for i in range(125)]
                            for item in sublist],
    'lstm_model_time_period': [item for sublist in
                               [[2, 3, 5, 7, 9, 3, 2, 7, 5, 9]
                                for i in range(250)]
                               for item in sublist],
}

# VISUALIZATION TYPES
visualization_types_data = {
    'name': [
        "BACKTEST_SIGNALS",
        "BACKTEST_TRADE",
        "PAPER_TRADE",
    ],
    'description': [
        "Contains Company data, Indicators and Signals generated in a backtest",
        "Contains Company data, Indicators and Trade data (entry and exit orders) of a backtest trade",
        "Contains Company data, Indicators and Trade data (entry and exit orders) of a paper trade"
    ],
}

# EXAMPLE BACKTESTER DATA
example_backtester_data = {
    'name': [
        'hello-backtester'
    ]
}

# RUN BACKTESTS DATA FOR BB STRATEGY
run_backtests_data = {
    'date_ranges': [
        ['2017-01-01 00:00:00+00:00', '2020-12-30 00:00:00+00:00']
        for i in range(40)
    ],
    'ticker_time_periods': [
        "1"
        for i in range(40)
    ],
    'indicators': [
        BollingerIndicator
        for i in range(40)
    ],
    'signal_generators': [
        BBSignalGenerator
        for i in range(40)
    ],
    'take_profit_and_stop_losses': [
        TakeProfitAndStopLossBB
        for i in range(40)
    ],
    'order_executors': [
        OrderExecution
        for i in range(40)
    ],
    'trade_evaluators': [
        TradeEvaluator
        for i in range(40)
    ],
}

# EXAMPLE PAPERTRADER DATA
example_papertrader_data = {
    'name': [
        'hello-papertrader'
    ]
}

# PAPER TRADED STRATEGY DATA
paper_traded_strategy_data = {}


class InitializeDatabase(object):

    def run(self):
        # Set starting time
        start = time.time()

        print("STARTING DATABASE INITIALIZATION SERVICE")
        print("Please be patient, this may take a while...")

        # Cleaning DB of all data
        CleanDatabase().run()

        # Initialize DB Users
        User.objects.create_superuser(
            username='superuser',
            password='superuser1234'
        )

        User.objects.create_superuser(
            username='guest',
            password='guest1234'
        )

        print("STEP 2: Added a guest user and a super user")

        # Initialize strategies models

        # Add example strategies data to DB
        AddDBObject(
            step=3,
            msg="Added Example Strategy to DB",
            obj=ExampleStrategiesModel,
            obj_data=example_strategies_data,
        ).run()

        # Add companies to DB
        AddCompanies(
            step=4,
        ).run()

        # Add companies data to DB
        AddCompaniesData(
            step=5,
            # stop_point=1,
        ).run()

        # Add indicator types to DB
        AddDBObject(
            step=6,
            msg="Added Indicator Types to DB",
            obj=IndicatorType,
            obj_data=indicator_types_data,
        ).run()

        # Add Strategy Types to DB
        AddDBObject(
            step=7,
            msg="Added Strategy Types to DB",
            obj=StrategyType,
            obj_data=strategy_types_data,
        ).run()

        # Fix BB strategy config foreign keys
        st = StrategyType.objects.all()[0]
        c = Company.objects.all()[0]
        bb_strategy_configs_data['strategy_type'] = [st for i in range(20)]
        bb_strategy_configs_data['lstm_company'] = [c for i in range(20)]

        # Add Strategy Configs for BB Strategy to DB
        AddDBObject(
            step=8,
            msg="Added BB Strategy Configs to DB",
            obj=StrategyConfig,
            obj_data=bb_strategy_configs_data,
        ).run()

        # Fix LSTM strategy config foreign keys
        st = StrategyType.objects.all()[1]
        lstm_strategy_configs_data['strategy_type'] = [st for i in range(2500)]
        lstm_strategy_configs_data['lstm_company'] = [item for sublist in
                                                      [[Company.objects.all()[i] for j in range(50)] for i in range(50)]
                                                      for item in sublist]

        # Add Strategy Configs for LSTM Strategy to DB
        AddDBObject(
            step=9,
            msg="Added LSTM Strategy Configs to DB",
            obj=StrategyConfig,
            obj_data=lstm_strategy_configs_data,
        ).run()

        # Initialize Backtester Models

        # Add example backtester data to DB
        AddDBObject(
            step=10,
            msg="Added Example Backtester to DB",
            obj=ExampleBackTesterModel,
            obj_data=example_backtester_data,
        ).run()

        # Add Visualization Types to DB
        AddDBObject(
            step=11,
            msg="Added Visualization Types to DB",
            obj=VisualizationType,
            obj_data=visualization_types_data,
        ).run()

        # Run Backtests
        AutomatedBacktests(
            step=12,
            msg="Ran Backtests and added reports to DB",
            data=run_backtests_data,
        ).run()

        # Initialize Paper traded Models

        # Add example papertrader data to DB
        AddDBObject(
            step=13,
            msg="Added Example PaperTrader to DB",
            obj=ExamplePaperTraderModel,
            obj_data=example_papertrader_data,
        ).run()

        # Update paper trade strategies
        num_of_paper_traded_strategies = 2000

        paper_traded_strategy_data['company'] = [item for sublist in
                                                 [[item for sublist in
                                                   [[company for i in range(20)]
                                                    for company in list(Company.objects.all())]
                                                   for item in sublist]
                                                  for i in range(2)]
                                                 for item in sublist]

        paper_traded_strategy_data['strategy_config'] = [item for sublist in
                                                         [list(StrategyConfig.objects.filter(
                                                             strategy_type__name='Simple Bollinger Band Strategy'
                                                         ))
                                                             for i in range(len(list(Company.objects.all())))]
                                                         for item in sublist]

        paper_traded_strategy_data['strategy_config'] += [item for sublist in
                                                          [list(StrategyConfig.objects.filter(
                                                              strategy_type__name='LSTM Strategy',
                                                              lstm_company=company,
                                                          ))
                                                              for company in list(Company.objects.all())]
                                                          for item in sublist]

        paper_traded_strategy_data['live'] = [True for i in range(num_of_paper_traded_strategies)]

        # Add Live Paper Traded Strategies
        AddDBObject(
            step=14,
            msg="Added PaperTradedStrategy to DB",
            obj=PaperTradedStrategy,
            obj_data=paper_traded_strategy_data,
        ).run()

        # Run Paper Trade Synchronizer once
        print("STEP 15: Runnning the paper trade algorithm. Please wait, this may take a while...")
        PaperTradeSynchronizer().run()
        print("STEP 15: Successfully Ran Paper Trade Algorithm")

        # Set end time
        end = time.time()

        # print time taken
        print(f"Completed Database Initialization in {end - start} seconds")
