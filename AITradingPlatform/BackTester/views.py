import json
import sys
from datetime import datetime
from datetime import timedelta
import pandas as pd

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.timezone import make_aware

from .models import ExampleBackTesterModel, BackTestReport, BackTestOrder
from .serializers import ExampleBackTesterSerializer
from Strategies.utils import simple_bollinger_bands_strategy
from Strategies.models import Strategy, Orders

from DataFeeder.models import Company, ImmutableData, Indicators
from DataFeeder.utils import get_data_on_demand, push_indicators_to_db


@api_view(['GET', ])
def api_index(req, slug):
    print("Example Back Tester Model slug:", slug)

    try:
        name = ExampleBackTesterModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExampleBackTesterSerializer(name).data)


@api_view(['POST', ])
def api_generate_report(req):

    req_body = json.loads(req.body)
    print(req_body)

    # create response if request not valid
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # list of allowed slices
    allowed_slices = [f'year{year}month{month}' for year in range(1, 3) for month in range(1, 13)]

    try:
        valid_risk_ratio = 'risk_ratio' in req_body and type(req_body['risk_ratio']) == str
        valid_max_risk = 'max_ratio' in req_body and type(req_body['max_risk']) == float
        valid_initial_acc = 'initial_acc' in req_body and type(req_body['initial_acc']) == float
        valid_strategy = 'strategy' in req_body and req_body['strategy'] in ['Simple Bollinger Bands Strategy']
        valid_company = type(req_body['candlestick_data']['company']) == str
        valid_provider = req_body['candlestick_data']['company'] in ['Yahoo', 'Alpha']
        start_dt = make_aware(datetime.strptime(req_body['candlestick_data']['start_date'], '%Y-%m-%d %H:%M:%S'))
        end_dt = make_aware(datetime.strptime(req_body['candlestick_data']['end_date'], '%Y-%m-%d %H:%M:%S'))
        valid_time_period = req_body['candlestick_data']['time_period'] in ['daily', '60min', '30min', '15min', '10min',
                                                                            '5min', '1min']
        valid_slice = req_body['candlestick_data']['slice'] in allowed_slices
        valid_column = req_body['indicators_data']['column'] in ['Close', 'Open', 'High', 'Low', 'Volume']
        valid_sigma = type(req_body['indicators_data']['sigma']) == int
        valid_indicator_time_period = type(req_body['indicators_data']['time_period']) == int

    except Exception as e:

        print("Exception occured: ", e)

        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)
        res = {'status': 'Invalid'}
        return JsonResponse(res)


    # Extract data from req
    strategy = req_body['strategy']
    company = req_body['candlestick_data']['company']
    provider = req_body['candlestick_data']['provider']
    candle_stick_time_period = req_body['candlestick_data']['time_period']
    slice = req_body['candlestick_data']['slice']
    column = req_body['indicators_data']['column']
    indicator_time_period = req_body['indicators_data']['time_period']
    sigma = req_body['indicators_data']['sigma']
    risk_ratio = req_body['risk_ratio']
    max_risk = req_body['max_risk']
    initial_acc = req_body['initial_acc']

    collected_data, data_not_collected, df = simple_bollinger_bands_strategy(company, provider, start_dt, end_dt,
                                                                             candle_stick_time_period, slice, column,
                                                                             indicator_time_period, sigma)
    print(df)
    print(df.columns.tolist())

    profit = []
    loss = []
    #print(column)

    company_obj = Company.objects.get(ticker=company)
    strategy_obj = Strategy.objects.get(name=req_body['strategy'])

    df['order_owner'] = None
    df['profit'] = None
    df['quantity'] = None
    df['acc_size'] = None
    df['price'] = None
    flag = 0
    pos = []
    for i in range(len(df)):

        flag += 1
        pos.append(i)

        price = 0

        if (df['Orders'][i] == "GET_OUT_OF_ALL_POSITIONS"):
            pos.pop()
            flag -= 1
            print(pos,flag-1)

            date1 = df.index[i].to_pydatetime()
            date1 += timedelta(days=1)
            data1 = ImmutableData.objects.filter(company=company_obj, time_stamp=date1)

            if data1.exists():
                print("exists")
            else:
                while (data1.exists() == False):
                    date1 += timedelta(days=1)
                    data1 = ImmutableData.objects.filter(company=company_obj, time_stamp=date1)
            close_get_out_position = []
            close_get_out_position.append(data1.values('close')[0])
            close_get_out_position1 = []
            for k in close_get_out_position[0].values():
                close_get_out_position1.append(k)
            close_price1 = close_get_out_position1[0]
            df['quantity'][i] = int((initial_acc - (max_risk * initial_acc)) / close_price1)
            df['price'][i] = 0

            for j in range(len(pos)):
                date = df.index[pos[j]].to_pydatetime()
                # to get the next day

                date += timedelta(days=1)
                #print(date)
                # collected_data, data_not_found = get_data_on_demand(company, provider,
                #                                                     start_dt, end_dt, indicator_time_period,
                #                                                     slice)
                # print(collected_data,data_not_found)

                data = ImmutableData.objects.filter(company=company_obj, time_stamp=date)

                if (data.exists()==False):
                    while(data.exists() == False):
                        date += timedelta(days=1)
                        data = ImmutableData.objects.filter(company=company_obj, time_stamp=date)
                        #print(date,data)
                print(date, data)
                # print(df[column][pos[j]])
                # print(df[column][i])

                # if (df['Orders'] == "SHORT"):
                #     print("yes")
                close=[]
                close.append(data.values('close')[0])
                close1 = []
                for k in close[0].values():
                    close1.append(k)
                close_price =close1[0]
                df['quantity'][pos[j]] = int((initial_acc - (max_risk * initial_acc)) / close_price)
                price = 0
                if (df['Orders'][pos[j]] == "SHORT") :
                    # print("short")
                    # print(df[column][i],df[column][pos[j]], (df[column][i] - df[column][pos[j]]))
                    price = float((df[column][i] - close_price) * -1)
                    df['price'][pos[j]] = price
                    if price > 0:
                        df['profit'][pos[j]] = "Profit"
                    if price < 0:
                        df['profit'][pos[j]] = "Loss"
                    if pos[j] == 0:
                        df['acc_size'][pos[j]] = (df['quantity'][pos[j]] * price ) + initial_acc
                    else:
                        df['acc_size'][pos[j]] = (df['quantity'][pos[j]] * price) + df['acc_size'][pos[j] - 1]
                if (df['Orders'][pos[j]] == "BUY") :
                    # print("buy")
                    # print(df[column][i],df[column][pos[j]], (df[column][i] - df[column][pos[j]]))
                    price = float(df[column][i] - close_price)
                    df['price'][pos[j]] = price
                    if price > 0:
                        df['profit'][pos[j]] = "Profit"
                    if price < 0:
                        df['profit'][pos[j]] = "Loss"
                    if pos[j] == 0:
                        df['acc_size'][pos[j]] = (df['quantity'][pos[j]] * price ) + initial_acc
                    else:
                        df['acc_size'][pos[j]] = (df['quantity'][pos[j]] * price) + df['acc_size'][pos[j] - 1]

            df['acc_size'][i] = df['quantity'][i] + df['acc_size'][i - 1]

            flag = 0
            pos.clear()

            # print(list(map(int, risk_ratio.split(":"))))
            df['order_owner'] = "Bactester"
            # print(df.iloc[i])

        Orders(

            order_type = df['Orders'][i],
            order_category = 'Limit',
            company = company_obj,
            time_stamp = df.index[i].to_pydatetime(),
            profit_loss = df['price'][i],
            quantity = df['quantity'][i],
            ).save()
        order_obj = Orders.objects.get(order_type = df['Orders'][i])
        backtest_obj = BackTestReport.objects.get(company=company_obj, start_date_time= start_dt, end_date_time= end_dt, max_risk = max_risk, risk_ratio = risk_ratio,\
                                               initial_account_size = initial_acc, final_account_size = final_acc_size,total_profit_loss = total_PF,strategy = strategy_obj)
        BackTestOrder(
            order=order_obj,
            backtestreport = backtest_obj,
            account_size = df['acc_size'][i]
        )


    final_acc_size = df['acc_size'][len(df)-1]
    total_PF = df['acc_size'][len(df)-1] - initial_acc
    print(total_PF,final_acc_size)

    # print(df.columns.tolist())
    print(df)

    if not BackTestReport.objects.all().filter(company=company_obj, start_date_time= start_dt, end_date_time= end_dt, max_risk = max_risk, risk_ratio = risk_ratio,\
                                               initial_account_size = initial_acc, final_account_size = final_acc_size,total_profit_loss = total_PF,strategy = strategy_obj):
        BackTestReport(
            start_date_time=start_dt,
            end_date_time = end_dt,
            max_risk = max_risk,
            risk_ratio = risk_ratio,
            initial_account_size = initial_acc,
            final_account_size = final_acc_size,
            total_profit_loss = total_PF,
            company = company_obj,
            strategy = strategy_obj,
        ).save()
    # if not Indicators.objects.all().filter(column=column,indicator_time_period= indicator_time_period):
    #     Indicators(
    #         name=
    #     value = models.FloatField(default=0.0)
    #     column = models.CharField(max_length=20, default='Default')
    #     indicator_time_period = models.IntegerField(default=0)
    #     candle_stick = models.ForeignKey(to=ImmutableData, on_delete=models.CASCADE, blank=True)
    #     ).save()



    # push_indicators_to_db(df, f'{column}_{indicator_time_period}', company_obj, indicator_time_period,
    #                       candle_stick_time_period, column)
    res = {'status': "Valid"}

    return JsonResponse(res)
