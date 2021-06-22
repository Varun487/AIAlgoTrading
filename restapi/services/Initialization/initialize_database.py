from pandas_datareader import data as pd_data_reader
import pandas as pd
import psycopg2

print()
print("INITIALIZING DB")

#################### SETUP DATABASE CONNECTION ####################
print()
print("----------STEP 1----------")
print()

print("Setting up DB connection...")

# Set up database connection
conn = psycopg2.connect(
    host="db",
    database="postgres",
    user="postgres",
    password="postgres",
    port=5432,
)

# setup cursor
cur = conn.cursor()

print("Connected to DB")

#################### CLEAN UP ALL PREVIOUS DATA IN DB ####################
print()
print("----------STEP 2----------")
print()

print("Cleaning up all data in DB...")


def delete_table(package, table):
    # Delete all rows from the given table
    cur.execute(f"DELETE FROM {package}_{table}")
    conn.commit()


tables_dict = {
    'backtester': ['BackTestTrade', 'BackTestReport'],
    'strategies': ['VisualizationType', 'Trade', 'Order', 'Signal', 'StrategyConfig', 'StrategyType', 'IndicatorType',
                   'TickerData', 'Company']
}

for package in tables_dict:
    for table in tables_dict[package]:
        delete_table(package, table)

print("DB cleaned and set up")

#################### SETUP COMPANY TABLE IN DB ####################
print()
print("----------STEP 3----------")
print()

print("Adding companies to DB...")

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
    cur.execute(
        f"INSERT INTO strategies_Company VALUES ({company + 1}, '{company_name}', '{company_ticker}', '{company_description}');"
    )
    conn.commit()

print("Completed adding companies to DB")

#################### SOURCE DATA FROM YAHOO FINANCE AND PUSH TO DB ####################
print()
print("----------STEP 4----------")
print()

print("Sourcing data from Yahoo! Finance and pushing it to DB...")
print()

# To keep track of ids
ticker_data_id_counter = 1

# iterate through all companies
for ticker in range(len(nifty_companies)):
    print(f"Company {ticker + 1}/50")
    print(f"Sourcing data for: {nifty_companies['Symbol'][ticker] + '.NS'}")
    print()

    # source data for these companies from Yahoo finance from 2017-01-01 to 2020-12-31
    sourced_data = pd_data_reader.DataReader(nifty_companies['Symbol'][ticker] + '.NS', 'yahoo', '2017-01-01',
                                             '2020-12-30')

    for ticker_data in range(len(sourced_data)):

        # extract company data
        open = sourced_data['Open'][ticker_data]
        high = sourced_data['High'][ticker_data]
        low = sourced_data['Low'][ticker_data]
        close = sourced_data['Close'][ticker_data]
        volume = sourced_data['Volume'][ticker_data]
        time_stamp = sourced_data.index[ticker_data]
        company = ticker + 1

        # push data to db
        cur.execute(
            f"INSERT INTO strategies_TickerData VALUES({ticker_data_id_counter}, {open}, {high}, {low}, {close}, {volume}, '{time_stamp}', 1,  {company});"
        )
        conn.commit()

        # update id counter
        ticker_data_id_counter += 1

        # temporary breaks, to be removed when running whole script
        if ticker_data == 4:
            break

    # temporary breaks, to be removed when running whole script
    if ticker == 4:
        break

print("Completed")

#################### ADD INDICATOR TYPES TO DB ####################
print()
print("----------STEP 5----------")
print()

print("Adding indicator types to DB...")

indicator_names = ['Bollinger Bands Indicator']
indicator_description = [
    'The indicator used for the Simple Bollinger bands strategy. Calculates the Simple Moving Average and n standard deviations above and below the simple moving average',
]

for indicator in range(len(indicator_names)):
    cur.execute(
        f"INSERT INTO strategies_IndicatorType VALUES({indicator + 1}, '{indicator_names[indicator]}', '{indicator_description[indicator]}');"
    )
    conn.commit()

print("Completed")

#################### ADD STRATEGY TYPES TO DB ####################
print()
print("----------STEP 6----------")
print()

print("Adding strategy types to DB...")

strategy_names = ['Simple Bollinger Band Strategy']
strategy_descriptions = ['This strategy uses the Bollinger Bands indicator to generate signals.']
strategy_stock_selections = ['All Stocks / Crypto / Forex / Commodities applicable.']
strategy_entry_criterias = [
    'BUY signal if stock price < n std. dev below SMA. SELL signal if stock price > n std. dev above SMA.',
]
strategy_exit_criterias = ['If stock held for the max holding period or price crosses take profit or stop loss limits.']
strategy_stop_loss_methods = [
    '((close price of previous candlestick - current close price) * factor) is added or subtracted from current close price',
]
strategy_take_profit_methods = [
    '((close price of previous candlestick - current close price) * factor) is added or subtracted from current close price'
]

for strategy_type in range(len(strategy_names)):
    cur.execute(
        f"INSERT INTO strategies_StrategyType VALUES({strategy_type + 1}, '{strategy_names[strategy_type]}', "
        f"'{strategy_descriptions[strategy_type]}',  '{strategy_stock_selections[strategy_type]}', "
        f"'{strategy_entry_criterias[strategy_type]}', '{strategy_exit_criterias[strategy_type]}', "
        f"'{strategy_stop_loss_methods[strategy_type]}', '{strategy_take_profit_methods[strategy_type]}');"
    )
    conn.commit()

print("Completed")

#################### ADD STRATEGY CONFIGS TO DB ####################
print()
print("----------STEP 7----------")
print()

print("Adding strategy configs to DB...")

strategy_types = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
indicator_time_periods = [5, 5, 5, 10, 10, 10, 15, 20, 20, 20]
max_holding_periods = [5, 5, 5, 7, 7, 7, 14, 14, 14, 21]
take_profit_factors = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
stop_loss_factors = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
sigmas = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
dimensions = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]

for strategy_config in range(len(strategy_types)):
    cur.execute(
        f"INSERT INTO strategies_StrategyConfig "
        f"VALUES({strategy_config + 1}, "
        f"'{indicator_time_periods[strategy_config]}',  '{max_holding_periods[strategy_config]}', "
        f"'{take_profit_factors[strategy_config]}', '{stop_loss_factors[strategy_config]}', "
        f"'{sigmas[strategy_config]}', '{dimensions[strategy_config]}', {strategy_types[strategy_config]});"
    )
    conn.commit()

print("Completed")

#################### RUN BACKTESTS ####################
print()
print("----------STEP 8----------")
print()

print("Running all backtests...")

print("NOT completed")

#################### ADD VISUALIZATION TYPES TO DB ####################
print()
print("----------STEP 9----------")
print()

print("Adding Visualization Types to DB...")

print("NOT completed")

#################### CLOSE DB CONNECTION ####################
print()
print("----------STEP 10----------")
print()

cur.close()
conn.close()

print("Closed connection to db")
print()
print("----------------------------")

print()
print("DB INITIALIZATION COMPLETE")
print()
