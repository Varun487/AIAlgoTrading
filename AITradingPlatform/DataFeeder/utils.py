import sys
from .models import Company, ImmutableData, Indicators
import pandas_datareader.data as web
from os import environ
import pandas as pd
from django.utils.timezone import make_aware
from math import isnan

pd.options.mode.chained_assignment = None


# FUNCTION TO CALCULATE SIMPLE MOVING AVERAGE INDICATOR, GIVEN A DATAFRAME

def df_simple_moving_average(df, time_period, column):
    df[f"SMA_{column}_{time_period}"] = df[column].rolling(window=time_period).mean()
    return df


# FUNCTION TO CALCULATE STANDARD DEVIATION INDICATOR, GIVEN A DATAFRAME

def df_std_dev(df, time_period, column):
    # Calculate standard deviation
    std_dev = df[column].rolling(window=time_period).std()

    # Std Dev.
    df[f"Std_Dev_{column}_{time_period}"] = std_dev

    # Calculate bollinger bands
    df[f"BB_up_1_{column}_{time_period}"] = df[f"SMA_{column}_{time_period}"] + std_dev
    df[f"BB_up_2_{column}_{time_period}"] = df[f"SMA_{column}_{time_period}"] + 2 * std_dev
    df[f"BB_up_3_{column}_{time_period}"] = df[f"SMA_{column}_{time_period}"] + 3 * std_dev
    df[f"BB_down_1_{column}_{time_period}"] = df[f"SMA_{column}_{time_period}"] - std_dev
    df[f"BB_down_2_{column}_{time_period}"] = df[f"SMA_{column}_{time_period}"] - 2 * std_dev
    df[f"BB_down_3_{column}_{time_period}"] = df[f"SMA_{column}_{time_period}"] - 3 * std_dev

    return df


# FUNCTION TO CALCULATE ALL INDICATORS, FOR A GIVEN DATAFRAME

def calc_indicators(df, time_period, column):
    # Calculate SMA
    df = df_simple_moving_average(df, time_period, column)

    # Calculate std dev
    df = df_std_dev(df, time_period, column)

    return df


# FUNCTION TO PUSH INDICATORS DATA TO DB, IF NOT PRESENT IN DB

def push_indicators_to_db(df, name, company_obj, indicator_time_period, company_time_period, column):
    all_indicators_data = Indicators.objects.all().filter(name=name, indicator_time_period=indicator_time_period, column=column)
    all_immutable_data = ImmutableData.objects.all().filter(company=company_obj, time_period=company_time_period)

    for i in range(len(df.index)):
        candle_stick = all_immutable_data.filter(time_stamp=df.index[i])
        # print(candle_stick)
        # print(all_indicators_data.filter(candle_stick=candle_stick[0]))
        # print(candle_stick and not all_indicators_data.filter(candle_stick=candle_stick[0]) and not isnan(df[name][i]))
        if candle_stick and not all_indicators_data.filter(candle_stick=candle_stick[0]) and not isnan(df[name][i]):
            Indicators(
                name=name,
                value=df[name][i],
                column=column,
                indicator_time_period=indicator_time_period,
                candle_stick=candle_stick[0],
            ).save()


# FUNCTION TO PUSH IMMUTABLE DATA TO DB, IF NOT PRESENT IN DB

def push_immutable_data_to_db(df, company_obj, time_period):
    all_immutable_data = ImmutableData.objects.all().filter(company=company_obj, time_period=time_period)

    for i in range(len(df)):

        if not all_immutable_data.filter(time_stamp=df.index[i]):
            ImmutableData(
                time_stamp=df.index[i],
                company=company_obj,
                open=df.Open[i],
                high=df.High[i],
                low=df.Low[i],
                close=df.Close[i],
                volume=df.Volume[i],
                time_period=time_period,
            ).save()


# FUNCTION TO GET DATA ON DEMAND

def get_data_on_demand(companies, provider, start_dt, end_dt, time_period, slice):
    collected_data = []
    data_not_found = []

    # collect data per company
    for company in companies:

        try:
            # company must exist in DB to collect data
            company_obj = Company.objects.get(ticker=company)

            # collect yahoo finance data
            if provider == 'Yahoo':

                # collect data
                df = web.DataReader(f"{company}", 'yahoo', start_dt, end_dt)

                df = df.reset_index()

                df['Date'] = pd.to_datetime(df['Date'])
                for date in range(len(df.index)):
                    df['Date'][date] = make_aware(df['Date'][date])

                df.set_index('Date', inplace=True)

            # collect AlphaVantage data
            else:

                url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={company}&interval={time_period}&slice={slice}&adjusted=false&apikey={environ["API_KEY"]}'

                df = pd.read_csv(url)
                df['time'] = pd.to_datetime(df['time'])

                for date in range(len(df.index)):
                    df['time'][date] = make_aware(df['time'][date])

                df = df[start_dt <= df.time]
                df = df[df.time <= end_dt]
                df.set_index('time', inplace=True)

                for col in df.columns:
                    df.rename(columns={col: col.capitalize()}, inplace=True)

                # Put dates in ascending order
                df = df.iloc[::-1]

            df = calc_indicators(df, 5, 'Close')

            push_immutable_data_to_db(df, company_obj, time_period)

            push_indicators_to_db(df, 'SMA_Close_5', company_obj, 5, time_period, 'Close')
            push_indicators_to_db(df, 'Std_Dev_Close_5', company_obj, 5, time_period, 'Close')

            push_indicators_to_db(df, 'BB_up_1_Close_5', company_obj, 5, time_period, 'Close')
            push_indicators_to_db(df, 'BB_up_2_Close_5', company_obj, 5, time_period, 'Close')
            push_indicators_to_db(df, 'BB_up_3_Close_5', company_obj, 5, time_period, 'Close')

            push_indicators_to_db(df, 'BB_down_1_Close_5', company_obj, 5, time_period, 'Close')
            push_indicators_to_db(df, 'BB_down_2_Close_5', company_obj, 5, time_period, 'Close')
            push_indicators_to_db(df, 'BB_down_3_Close_5', company_obj, 5, time_period, 'Close')

            collected_data.append(company)

        except Exception as e:

            print("Exception occured: ", e)

            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print("Exception type: ", exception_type)
            print("File name: ", filename)
            print("Line number: ", line_number)

            data_not_found.append(company)

    return collected_data, data_not_found
