import time

from django.contrib.auth.models import User

# Get all services required
from services.Initialization.clean_database import CleanDatabase
from services.Initialization.add_companies import AddCompanies
from services.Initialization.add_companies_data import AddCompaniesData
from services.Initialization.add_db_object import AddDBObject
from services.Initialization.automated_backtests import AutomatedBacktests

from services.IndicatorCalc.indicators import BollingerIndicator
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.OrderExecution.orderexecution import OrderExecution
from services.TradeEvaluation.tradeevaluator import TradeEvaluator
from services.PaperTradeSynchronizer.papertradesynchronizer import PaperTradeSynchronizer

# Get all models required
from strategies.models import ExampleStrategiesModel
from strategies.models import Company
from strategies.models import IndicatorType
from strategies.models import StrategyType
from strategies.models import StrategyConfig
from strategies.models import VisualizationType

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
        'Bollinger Bands Indicator'
    ],
    'description': [
        'The indicator used for the Simple Bollinger bands strategy. Calculates the Simple Moving Average and n '
        'standard deviations above and below the simple moving average',
    ]
}

# STRATEGY TYPES DATA
strategy_types_data = {
    'name': [
        'Simple Bollinger Band Strategy',
    ],
    'description': [
        'This strategy uses the Bollinger Bands indicator to generate signals.',
    ],
    'stock_selection': [
        'All Stocks / Crypto / Forex / Commodities applicable.',
    ],
    'entry_criteria': [
        'BUY signal if stock price < n std. dev below SMA. SELL signal if stock price > n std. dev above SMA.',
    ],
    'exit_criteria': [
        'If stock held for the max holding period or price crosses take profit or stop loss limits.',
    ],
    'stop_loss_method': [
        '((close price of previous candlestick - current close price) * factor) is added or subtracted from current '
        'close price',
    ],
    'take_profit_method': [
        '((close price of previous candlestick - current close price) * factor) is added or subtracted from current '
        'close price',
    ],
}

# STRATEGY CONFIGS DATA
strategy_configs_data = {
    'strategy_type': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'indicator_time_period': [5, 5, 5, 10, 10, 10, 15, 15, 15, 20],
    'max_holding_period': [5, 5, 5, 7, 7, 7, 14, 14, 14, 21],
    'take_profit_factor': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    'stop_loss_factor': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    'sigma': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    'dimension': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2],
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

# RUN BACKTESTS DATA
run_backetests_data = {
    'date_ranges': [
        ['2017-01-01 00:00:00+00:00', '2020-12-30 00:00:00+00:00']
        for i in range(10)
    ],
    'ticker_time_periods': [
        "1"
        for i in range(10)
    ],
    'indicators': [
        BollingerIndicator
        for i in range(10)
    ],
    'signal_generators': [
        BBSignalGenerator
        for i in range(10)
    ],
    'take_profit_and_stop_losses': [
        TakeProfitAndStopLossBB
        for i in range(10)
    ],
    'order_executors': [
        OrderExecution
        for i in range(10)
    ],
    'trade_evaluators': [
        TradeEvaluator
        for i in range(10)
    ],
}

# EXAMPLE PAPERTRADER DATA
example_papertrader_data = {
    'name': [
        'hello-papertrader'
    ]
}

# PAPER TRADED STRATEGY DATA
paper_traded_strategy_data = {
    'strategy_config': [],
    'company': [],
    'live': [],
}


class InitializeDatabase(object):

    def run(self):
        # Set starting time
        start = time.time()

        print("STARTING DATABASE INITIALIZATION SERVICE")
        print("Please be patient, this may take a while...")

        # Cleaning DB of all data
        CleanDatabase().run()

        # Initialize strategies models

        # Add example strategies data to DB
        AddDBObject(
            step=2,
            msg="Added Example Strategy to DB",
            obj=ExampleStrategiesModel,
            obj_data=example_strategies_data,
        ).run()

        # Add companies to DB
        AddCompanies(
            step=3,
        ).run()

        # Add companies data to DB
        AddCompaniesData(
            step=4,
            stop_point=2,
        ).run()

        # Add indicator types to DB
        AddDBObject(
            step=5,
            msg="Added Indicator Types to DB",
            obj=IndicatorType,
            obj_data=indicator_types_data,
        ).run()

        # Add Strategy Types to DB
        AddDBObject(
            step=6,
            msg="Added Strategy Types to DB",
            obj=StrategyType,
            obj_data=strategy_types_data,
        ).run()

        # Fix strategy config foreign key to Strategy Type
        strategy_configs_data['strategy_type'] = [StrategyType.objects.all()[0] for i in range(10)]

        # Add Strategy Configs to DB
        AddDBObject(
            step=7,
            msg="Added Strategy Configs to DB",
            obj=StrategyConfig,
            obj_data=strategy_configs_data,
        ).run()

        # Add Visualization Types to DB
        AddDBObject(
            step=8,
            msg="Added Visualization Types to DB",
            obj=VisualizationType,
            obj_data=visualization_types_data,
        ).run()

        # Initialize Backtester Models

        # Add example backtester data to DB
        AddDBObject(
            step=9,
            msg="Added Example Backtester to DB",
            obj=ExampleBackTesterModel,
            obj_data=example_backtester_data,
        ).run()

        # Run Backtests
        AutomatedBacktests(
            step=10,
            msg="Ran Backtests and added reports to DB",
            data=run_backetests_data,
        ).run()

        # Initialize Paper traded Models

        # Add example papertrader data to DB
        AddDBObject(
            step=11,
            msg="Added Example PaperTrader to DB",
            obj=ExamplePaperTraderModel,
            obj_data=example_papertrader_data,
        ).run()

        # Update paper trade strategies
        num_of_paper_traded_strategies = len(list(Company.objects.all())) * len(list(StrategyConfig.objects.all()))

        paper_traded_strategy_data['company'] = [item for sublist in
                                                 [[company for i in range(len(list(StrategyConfig.objects.all())))]
                                                  for company in list(Company.objects.all())]
                                                 for item in sublist]

        paper_traded_strategy_data['strategy_config'] = [item for sublist in
                                                         [list(StrategyConfig.objects.all())
                                                          for i in range(len(list(Company.objects.all())))]
                                                         for item in sublist]

        paper_traded_strategy_data['live'] = [True for i in range(num_of_paper_traded_strategies)]

        # Add Live Paper Traded Strategies
        AddDBObject(
            step=11,
            msg="Added PaperTradedStrategy to DB",
            obj=PaperTradedStrategy,
            obj_data=paper_traded_strategy_data,
        ).run()

        # Run Paper Trade Synchronizer once
        print("STEP 12: Runnning the paper trade algorithm. Please wait, this may take a while...")
        PaperTradeSynchronizer().run()
        print("STEP 12: Successfully Ran Paper Trade Algorithm")

        # Initialize DB Users
        User.objects.create_superuser(
            username='superuser',
            password='superuser1234'
        )

        User.objects.create_superuser(
            username='guest',
            password='guest1234'
        )

        print("STEP 13: Added a guest user and a super user")

        # Set end time
        end = time.time()

        # print time taken
        print(f"Completed Database Initialization in {end - start} seconds")
