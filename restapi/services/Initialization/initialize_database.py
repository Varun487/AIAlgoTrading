from django.utils.timezone import make_aware
from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd

# Override default pandas data reader downloader
yf.pdr_override()

print()
print("INITIALIZING DB")

#################### SETUP STANDALONE DJANGO APP ####################
print()
print("----------STEP 1----------")
print()

from django import setup
from django.conf import settings

import sys

sys.path.append('/home/app/restapi/')

from restapi import restapi_settings_defaults

# Configuring settings to run a stand alone django application
settings.configure(restapi_settings_defaults)

# To initialize the new app
setup()

# Get all required models
from strategies.models import Company
from strategies.models import TickerData
from strategies.models import IndicatorType
from strategies.models import StrategyType
from strategies.models import StrategyConfig
from strategies.models import Signal
from strategies.models import Order
from strategies.models import Trade
from strategies.models import VisualizationType
from backtester.models import BackTestReport
from backtester.models import BackTestTrade

print("Set up Stand Alone Django App")

#################### CLEAN UP ALL PREVIOUS DATA IN DB ####################
print()
print("----------STEP 2----------")
print()


def delete_table_data(table_obj):
    table_obj.objects.all().delete()


all_tables = [
    BackTestTrade,
    BackTestReport,
    VisualizationType,
    Trade,
    Order,
    Signal,
    StrategyConfig,
    StrategyType,
    IndicatorType,
    TickerData,
    Company,
]

for table in all_tables:
    delete_table_data(table)

print("Removed all previous data in DB")

##################### SETUP COMPANY TABLE IN DB ####################
print()
print("----------STEP 3----------")
print()

# get all nifty 50 companies
nifty_companies = pd.read_csv('/home/app/restapi/services/Initialization/nifty50list.csv')

# iterate through all companies and insert them into database
for company in range(len(nifty_companies)):
    # extract data for each company
    company_name = nifty_companies['Company Name'][company] + " NSE"
    company_ticker = nifty_companies['Symbol'][company] + ".NS"
    company_description = f"Industry: {nifty_companies['Industry'][company]} " \
                          f"Series: {nifty_companies['Series'][company]} " \
                          f"ISIN Code: {nifty_companies['ISIN Code'][company]}"

    # insert company data to db
    Company(name=company_name, ticker=company_ticker, description=company_description).save()

print("Added companies to DB")

#################### SOURCE DATA FROM YAHOO FINANCE AND PUSH TO DB ####################
print()
print("----------STEP 4----------")
print()

print("Sourcing ticker data...")
print()

# iterate through all companies
for ticker in range(len(nifty_companies)):
    print(f"Company {ticker + 1}/50")
    print(f"Sourcing data for: {nifty_companies['Symbol'][ticker] + '.NS'}")
    print()

    # source data for these companies from Yahoo finance from 2017-01-01 to 2020-12-31
    sourced_data = pdr.get_data_yahoo(nifty_companies['Symbol'][ticker] + '.NS', start='2017-01-01',
                                      end='2020-12-30')

    for ticker_data in range(len(sourced_data)):
        # extract company data
        ticker_open_price = sourced_data['Open'][ticker_data]
        ticker_high_price = sourced_data['High'][ticker_data]
        ticker_low_price = sourced_data['Low'][ticker_data]
        ticker_close_price = sourced_data['Close'][ticker_data]
        ticker_volume = sourced_data['Volume'][ticker_data]
        ticker_time_stamp = sourced_data.index[ticker_data]
        ticker_time_stamp = make_aware(ticker_time_stamp)
        ticker_company = Company.objects.get(ticker=nifty_companies['Symbol'][ticker] + '.NS')
        ticker_time_period = "1"

        # push data to db
        TickerData(
            open=ticker_open_price,
            high=ticker_high_price,
            low=ticker_low_price,
            close=ticker_close_price,
            volume=ticker_volume,
            time_stamp=ticker_time_stamp,
            company=ticker_company,
            time_period=ticker_time_period,
        ).save()

    if ticker == 2:
        break

print("Sourced ticker data from Yahoo! Finance and pushed to DB")

# #################### ADD INDICATOR TYPES TO DB ####################
print()
print("----------STEP 5----------")
print()

indicator_names = ['Bollinger Bands Indicator']
indicator_description = [
    'The indicator used for the Simple Bollinger bands strategy. Calculates the Simple Moving Average and n standard deviations above and below the simple moving average',
]

for indicator in range(len(indicator_names)):
    IndicatorType(name=indicator_names[indicator], description=indicator_description[indicator]).save()

print("Added indicator types to DB")

#################### ADD STRATEGY TYPES TO DB ####################
print()
print("----------STEP 6----------")
print()

strategy_names = [
    'Simple Bollinger Band Strategy',
]
strategy_descriptions = [
    'This strategy uses the Bollinger Bands indicator to generate signals.',
]
strategy_stock_selections = [
    'All Stocks / Crypto / Forex / Commodities applicable.',
]
strategy_entry_criterias = [
    'BUY signal if stock price < n std. dev below SMA. SELL signal if stock price > n std. dev above SMA.',
]
strategy_exit_criterias = [
    'If stock held for the max holding period or price crosses take profit or stop loss limits.',
]
strategy_stop_loss_methods = [
    '((close price of previous candlestick - current close price) * factor) is added or subtracted from current close price',
]
strategy_take_profit_methods = [
    '((close price of previous candlestick - current close price) * factor) is added or subtracted from current close price',
]

for strategy_type in range(len(strategy_names)):
    StrategyType(
        name=strategy_names[strategy_type],
        description=strategy_descriptions[strategy_type],
        stock_selection=strategy_stock_selections[strategy_type],
        entry_criteria=strategy_entry_criterias[strategy_type],
        exit_criteria=strategy_exit_criterias[strategy_type],
        stop_loss_method=strategy_stop_loss_methods[strategy_type],
        take_profit_method=strategy_take_profit_methods[strategy_type],
    ).save()

print("Added strategy types to DB")

#################### ADD STRATEGY CONFIGS TO DB ####################
print()
print("----------STEP 7----------")
print()

strategy_types = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
indicator_time_periods = [5, 5, 5, 10, 10, 10, 15, 20, 20, 20]
max_holding_periods = [5, 5, 5, 7, 7, 7, 14, 14, 14, 21]
take_profit_factors = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
stop_loss_factors = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
sigmas = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
dimensions = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]

for strategy_config in range(len(strategy_types)):
    strategy_type = StrategyType.objects.get(name=strategy_names[strategy_types[strategy_config]])
    StrategyConfig(
        strategy_type=strategy_type,
        indicator_time_period=indicator_time_periods[strategy_config],
        max_holding_period=max_holding_periods[strategy_config],
        take_profit_factor=take_profit_factors[strategy_config],
        stop_loss_factor=stop_loss_factors[strategy_config],
        sigma=sigmas[strategy_config],
        dimension=dimensions[strategy_config],
    ).save()

print("Added strategy configs to DB")

# #################### ADD VISUALIZATION TYPES TO DB ####################
print()
print("----------STEP 8----------")
print()

visualization_names = [
    "SIGNALS",
    "ORDERS",
    "PER TRADE",
]
visualization_descriptions = [
    "Contains Company data, Indicators and Signals generated in the backtest",
    "Contains Company data, Indicators and Orders generated in the backtest",
    "Contains Company data, Indicators, Signals, Entry orders and Exit orders generated in the backtest",
]

for visualization in range(len(visualization_names)):
    VisualizationType(
        name=visualization_names[visualization],
        description=visualization_descriptions[visualization],
    ).save()

print("Added Visualization Types to DB")

#################### RUN BACKTESTS ####################
print()
print("----------STEP 9----------")
print()

from services.BackTestReportGeneration.backtestreportgenerator import BackTestReportGenerator
from services.Utils.getters import Getter
from services.IndicatorCalc.indicators import BollingerIndicator
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.OrderExecution.orderexecution import OrderExecution
from services.TradeEvaluation.tradeevaluator import TradeEvaluator

print("Running backtests...")

backtest_date_ranges = [
    ['2017-01-01 00:00:00+00:00', '2020-12-30 00:00:00+00:00']
    for i in range(10)
]
backtest_strategy_types = [
    StrategyType.objects.get(name='Simple Bollinger Band Strategy')
    for i in range(10)
]
backtest_ticker_time_periods = [
    "1"
    for i in range(10)
]
backtest_dimensions = ["close", "open", "high", "low", "close", "open", "high", "low", "close", "close"]
backtest_indicators = [
    BollingerIndicator
    for i in range(10)
]
backtest_signal_generators = [
    BBSignalGenerator
    for i in range(10)
]
backtest_strategy_configs = list(StrategyConfig.objects.all())
backtest_take_profit_and_stop_losses = [
    TakeProfitAndStopLossBB
    for i in range(10)
]
backtest_order_executors = [
    OrderExecution
    for i in range(10)
]
backtest_trade_evaluators = [
    TradeEvaluator
    for i in range(10)
]

backtest_count = 0

# Conduct backtests for each company
for company in Company.objects.all():

    # 10 backtests per company
    for i in range(10):
        df = Getter(TickerData, True, {
            "company": company,
            "time_stamp__range": backtest_date_ranges[i],
        }).get_data()
        if type(df) != list:
            df.drop(['id', 'company_id', 'time_period'], axis=1, inplace=True)
            df.set_index('time_stamp', inplace=True)
            df.reset_index(inplace=True)
            # print(df)
            backtest_count += 1
            print(f"Backtest: {backtest_count}/500 - {company} {backtest_strategy_configs[i]}")
            BackTestReportGenerator(
                df=df,
                ticker_time_period=backtest_ticker_time_periods[i],
                indicator_time_period=indicator_time_periods[i],
                dimension=backtest_dimensions[i],
                sigma=sigmas[i],
                factor=take_profit_factors[i],
                max_holding_period=max_holding_periods[i],
                company=company,
                strategy_type=backtest_strategy_types[i],
                indicator=backtest_indicators[i],
                strategy_config=backtest_strategy_configs[i],
                signal_generator=BBSignalGenerator,
                take_profit_stop_loss=backtest_take_profit_and_stop_losses[i],
                order_executor=backtest_order_executors[i],
                trade_evaluator=backtest_trade_evaluators[i]
            ).generate_backtest_report()

print("Ran all backtests")

#################### INTIALIZATION COMPLETE ####################
print()
print("--------------------------")
print()
print("DB INITIALIZATION COMPLETE")
print()
