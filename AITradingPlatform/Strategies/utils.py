import pandas as pd
from DataFeeder.utils import get_data_on_demand, calc_indicators, push_indicators_to_db
from DataFeeder.models import ImmutableData, Company, Indicators
from .models import Orders, Strategy


# SIMPLE BOLLINGER BANDS STRATEGY

# Get / Sources all data required for the strategy
# Converts to a df and returns
def create_df_simple_bollinger_bands_strategy(company, provider, start_dt, end_dt, candle_stick_time_period, slice,
                                              column, indicator_time_period, sigma):
    # initialize dataframe
    df = pd.DataFrame(pd.DataFrame(columns=['candle_stick_ids', column]))

    # Source data
    collected_data, data_not_found = get_data_on_demand([company], provider, start_dt, end_dt, candle_stick_time_period,
                                                        slice)

    # calculate indicators on data
    company_obj = Company.objects.get(ticker=company)

    candle_stick_data = ImmutableData.objects.filter(
        company=company_obj,
        time_stamp__range=[start_dt, end_dt],
        time_period=candle_stick_time_period,
    )

    column_data = []
    candle_stick_ids = []
    time_stamps = []

    for candle_stick in candle_stick_data:
        column_data.append(eval(f'candle_stick.{column.lower()}'))
        candle_stick_ids.append(candle_stick.id)
        time_stamps.append(candle_stick.time_stamp)

    df[column] = column_data
    df['candle_stick_ids'] = candle_stick_ids
    df['time_stamps'] = time_stamps

    df = calc_indicators(df, indicator_time_period, column)

    # transform dataframe to get required data
    # Push indicators data to db
    df.dropna(inplace=True)
    df.set_index('time_stamps', inplace=True)
    # df.reset_index(inplace=True)
    df = df[['candle_stick_ids', column, f'SMA_{column}_{indicator_time_period}',
             f'Std_Dev_{column}_{indicator_time_period}']]
    df[f'BB_up_{sigma}_{column}_{indicator_time_period}'] = df[f'SMA_{column}_{indicator_time_period}'] + sigma * df[
        f'Std_Dev_{column}_{indicator_time_period}']
    df[f'BB_down_{sigma}_{column}_{indicator_time_period}'] = df[f'SMA_{column}_{indicator_time_period}'] - sigma * df[
        f'Std_Dev_{column}_{indicator_time_period}']

    push_indicators_to_db(df, f'SMA_{column}_{indicator_time_period}', company_obj, indicator_time_period,
                          candle_stick_time_period, column)
    push_indicators_to_db(df, f'Std_Dev_{column}_{indicator_time_period}', company_obj, indicator_time_period,
                          candle_stick_time_period, column)
    push_indicators_to_db(df, f'BB_up_{sigma}_{column}_{indicator_time_period}', company_obj, indicator_time_period,
                          candle_stick_time_period, column)
    push_indicators_to_db(df, f'BB_down_{sigma}_{column}_{indicator_time_period}', company_obj, indicator_time_period,
                          candle_stick_time_period, column)

    return collected_data, data_not_found, df


# GENERATE ORDERS

# long positions
# short positions
# flat positions
# Get out of a position

def simple_bollinger_bands_strategy_generate_orders(df, column, indicator_time_period, sigma):
    orders = []
    position = "FLAT"

    for i in range(len(df)):
        price = df[column][i]
        sma = df[f'SMA_{column}_{indicator_time_period}'][i]
        up_band = df[f'BB_up_{sigma}_{column}_{indicator_time_period}'][i]
        down_band = df[f'BB_down_{sigma}_{column}_{indicator_time_period}'][i]
        # print(price, sma, up_band, down_band)

        if (position == "BUY" and price > sma) or (position == "SHORT" and price < sma):
            orders.append("GET_OUT_OF_ALL_POSITIONS")
            position = "FLAT"

        elif price > up_band:
            orders.append("SHORT")
            position = "SHORT"

        elif price < down_band:
            orders.append("BUY")
            position = "BUY"

        else:
            orders.append("FLAT")

    df['Orders'] = orders

    return df


# THE COMPLETE STRATEGY

def simple_bollinger_bands_strategy(company, provider, start_dt, end_dt, candle_stick_time_period, slice, column,
                                    indicator_time_period, sigma):
    collected_data, data_not_found, df = create_df_simple_bollinger_bands_strategy(company, provider, start_dt, end_dt,
                                                                                   candle_stick_time_period, slice,
                                                                                   column, indicator_time_period, sigma)

    df = simple_bollinger_bands_strategy_generate_orders(df, column, indicator_time_period, sigma)

    df = df[df.Orders != "FLAT"]

    # for i in range(len(df)):
    #     time_stamp = df.index[i]
    #     price = df[column][i]
    #     sma = df[f'SMA_{column}_{indicator_time_period}'][i]
    #     up_band = df[f'BB_up_1_{column}_{indicator_time_period}'][i]
    #     down_band = df[f'BB_down_1_{column}_{indicator_time_period}'][i]
    #     order = df['Orders'][i]
    #     print(time_stamp, price, sma, up_band, down_band, order)

    return collected_data, data_not_found, df
