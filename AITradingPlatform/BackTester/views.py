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

from .models import ExampleBackTesterModel
from .serializers import ExampleBackTesterSerializer
from Strategies.utils import simple_bollinger_bands_strategy

from DataFeeder.models import Company, ImmutableData
from DataFeeder.utils import get_data_on_demand


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
    final_acc = 0
    print("yes")
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

    company_obj = Company.objects.get(ticker=company)

    df['order_owner'] = None
    df['profit'] = None
    df['quantity'] = None
    df['acc_size'] = None
    flag = 0
    pos = []
    # for i in range(len(df)):
    #
    #     flag += 1
    #     pos.append(i)
    #
    #     #df['quantity'][i] = int((initial_acc - (max_risk * initial_acc)) / df[column][i])
    #
    #     if (df['Orders'][i] == "GET_OUT_OF_ALL_POSITIONS"):
    #         pos.pop()
    #         flag -= 1
    #         print(pos,flag-1)
    #         df['acc_size'][i] = df['quantity'] + df['acc_size'][i-1]
    #
    #         for j in range(len(pos)):
    #             date = df.index[pos[j]].to_pydatetime()
    #             # to get the next day
    #             # date += timedelta(days=1)
    #             # print(date)
    #             # collected_data, data_not_found = get_data_on_demand(company, provider,
    #             #                                                     start_dt, end_dt, indicator_time_period,
    #             #                                                     slice)
    #             # print(collected_data,data_not_found)
    #
    #             data = ImmutableData.objects.filter(company=company_obj, time_stamp=date)
    #
    #             # print(data)
    #             # print(df[column][pos[j]])
    #             # print(df[column][i])
    #
    #             # if (df['Orders'] == "SHORT"):
    #             #     print("yes")
    #             price = 0
    #             if (df['Orders'][pos[j]] == "SHORT") :
    #                 # print("short")
    #                 # print(df[column][i],df[column][pos[j]], (df[column][i] - df[column][pos[j]]))
    #                 price = float((df[column][i] - df[column][pos[j]]) * -1)
    #                 if price > 0:
    #                     df['profit'][pos[j]] = "Profit"
    #                 if price < 0:
    #                     df['profit'][pos[j]] = "Loss"
    #                 # if pos[j] == 0:
    #                 #     df['acc_size'][pos[j]] = (df['quantity'][pos[j]] * price ) + initial_acc
    #                 # else:
    #                 #     df['acc_size'][pos[j]] = (df['quantity'][pos[j]] * price) + df['acc_size'][i - 1]
    #             if (df['Orders'][pos[j]] == "BUY") :
    #                 # print("buy")
    #                 # print(df[column][i],df[column][pos[j]], (df[column][i] - df[column][pos[j]]))
    #                 price = float(df[column][i] - df[column][pos[j]])
    #                 if price > 0:
    #                     df['profit'][pos[j]] = "Profit"
    #                 if price < 0:
    #                     df['profit'][pos[j]] = "Loss"
    #                 # if pos[j] == 0:
    #                 #     df['acc_size'][pos[j]] = df[column][pos[j]] - initial_acc +price
    #                 # else:
    #                 #     df['acc_size'][pos[j]] = df[column][pos[j]] - df['acc_size'][pos[j-1]] + price
    #
    #
    #
    #         flag = 0
    #         pos.clear()
    #
    #         # print(list(map(int, risk_ratio.split(":"))))
    #         df['order_owner'] = "Bactester"
    #         # print(df.iloc[i])
    #
    #
    #
    #
    # total_PF = final_acc - initial_acc
    # print(final_acc)
    #
    # # print(df.columns.tolist())
    # print(df)
    # res = {'status': "Valid"}

    return JsonResponse(res)
