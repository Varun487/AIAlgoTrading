import os

from services.Utils.converter import Converter
from services.Utils.getters import Getter

from strategies.models import Company, IndicatorType, StrategyType, StrategyConfig, VisualizationType, TickerData, \
    Signal, Order, Trade
from backtester.models import BackTestReport, BackTestTrade

all_companies = list(Company.objects.all())
all_data_objs = [Company, IndicatorType, StrategyType, StrategyConfig, VisualizationType]
all_data_objs_path = ['COMPANIES', 'INDICATOR_TYPES', 'STRATEGY_TYPES', 'STRATEGY_CONFIG', 'VISUALIZATION_TYPES']
all_data_objs_message = ['companies', 'indicator types', 'strategy types', 'strategy configs', 'visualization types']

all_data_by_company_objs = [TickerData, Signal, Order, Trade, BackTestReport, BackTestTrade]
all_data_by_company_objs_path = ['TICKER_DATA', 'SIGNALS', 'ORDERS', 'TRADES', 'BACKTEST_REPORTS', 'BACKTEST_TRADES']
all_data_by_company_objs_message = ['ticker', 'signal', 'order', 'trade', 'backtest reports', 'backtest_trades']
all_data_by_company_objs_company_filter_criteria = ['company', 'ticker_data__company', 'ticker_data__company',
                                                    'entry_order__ticker_data__company', 'company',
                                                    'back_test_report__company']
all_data_by_company_objs_time_stamp_filter_criteria = ['time_stamp', 'ticker_data__time_stamp',
                                                       'ticker_data__time_stamp',
                                                       'entry_order__ticker_data__time_stamp',
                                                       'start_date_time', 'back_test_report__start_date_time']


def get_all_data_from_DB(obj, path, message):
    df = Converter(obj_list=list(obj.objects.all())).to_df()
    df.to_csv(f'/home/app/restapi/STORAGE/{path}.csv', index=False)
    print(f"Got all {message} from DB")


def get_data_from_DB_by_company(obj, path, message, company_filter_criteria, time_stamp_filter_criteria):
    if path not in os.listdir(f'/home/app/restapi/STORAGE/'):
        os.mkdir(f'/home/app/restapi/STORAGE/{path}/')

    for company in all_companies:
        df = Getter(
            table_name=obj,
            df_flag=True,
            param_list={
                company_filter_criteria: company,
                f'{time_stamp_filter_criteria}__range': ['2017-01-01', '2020-12-31']
            }
        ).get_data()
        df.to_csv(f'/home/app/restapi/STORAGE/{path}/{company.ticker}.csv', index=False)
        print(f"Sourced data for {company.ticker}")

    print(f"Got all {message} data from DB by companies")


def source_and_store():
    """Source all data from DB and put in storage folder"""

    if 'STORAGE' not in os.listdir(f'/home/app/restapi/'):
        os.mkdir(f'/home/app/restapi/STORAGE')

    # Get data for objects where all data is required from DB
    for i in range(len(all_data_objs)):
        get_all_data_from_DB(all_data_objs[i], all_data_objs_path[i], all_data_objs_message[i])

    # Get data for objects where data by company is required from DB
    for i in range(len(all_data_by_company_objs)):
        get_data_from_DB_by_company(all_data_by_company_objs[i], all_data_by_company_objs_path[i],
                                    all_data_by_company_objs_message[i],
                                    all_data_by_company_objs_company_filter_criteria[i],
                                    all_data_by_company_objs_time_stamp_filter_criteria[i],)

    print('Completed Sourcing and Storing Data!')
