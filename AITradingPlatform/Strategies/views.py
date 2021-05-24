import json
from datetime import datetime

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.timezone import make_aware

from .models import ExampleStrategiesModel, Strategy , Orders

from .serializers import ExampleStrategiesSerializer, StrategySerializer , OrdersSerializer
from .utils import simple_bollinger_bands_strategy

@api_view(['GET', ])
def api_index(req, slug):
    print("Example Strategies Model slug:", slug)

    try:
        name = ExampleStrategiesModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExampleStrategiesSerializer(name).data)


@api_view(['POST', ])
def api_run_strategy(req):

    req_body = json.loads(req.body)
    # print(req_body)

    # Check req validity
    res = {
        "error": "invalid request, please check the documentation for the correct request format"
    }

    # list of allowed slices
    allowed_slices = [f'year{year}month{month}' for year in range(1, 3) for month in range(1, 13)]

    # checking validity of post req body

    try:
        valid_strategy = req_body['strategy'] in ['Simple Bollinger Bands Strategy']
        valid_company = type(req_body['candlestick_data']['company']) == str
        valid_provider = req_body['candlestick_data']['company'] in ['Yahoo', 'Alpha']
        start_dt = make_aware(datetime.strptime(req_body['candlestick_data']['start_date'], '%Y-%m-%d %H:%M:%S'))
        end_dt = make_aware(datetime.strptime(req_body['candlestick_data']['end_date'], '%Y-%m-%d %H:%M:%S'))
        valid_time_period = req_body['candlestick_data']['time_period'] in ['daily', '60min', '30min', '15min', '10min', '5min', '1min']
        valid_slice = req_body['candlestick_data']['slice'] in allowed_slices
        valid_column = req_body['indicators_data']['column'] in ['Close', 'Open', 'High', 'Low', 'Volume']
        valid_sigma = type(req_body['indicators_data']['sigma']) == int
        valid_indicator_time_period = type(req_body['indicators_data']['time_period']) == int
    except:
        return JsonResponse(res)

    # Return invalid request
    if valid_strategy and valid_company and valid_provider and valid_time_period and valid_slice and valid_column and valid_sigma and valid_indicator_time_period:
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

    if strategy == 'Simple Bollinger Bands Strategy':
        collected_data, data_not_collected, df = simple_bollinger_bands_strategy(company, provider, start_dt, end_dt,
                                                                             candle_stick_time_period, slice, column,
                                                                             indicator_time_period, sigma)
        if len(collected_data) == 1:
            res = {
                "status": "success, orders created",
                "strategy": "Simple Bollinger Bands Strategy",
                'collected_data': collected_data,
                'data_not_collected': data_not_collected
            }
        else:
            res = {
                "error": "Data not available and couldn't be sourced"
            }

    return JsonResponse(res)


@api_view(['POST', ])
def api_get_strategy(req):

    res = {'status': 'valid'}
    res['data'] = []

    data = Strategy.objects.all()
    res['data'] = StrategySerializer(data, many=True).data

    if not data:
        res = {
            'error': 'No data present in the db.'
        }

    return JsonResponse(res)
    # req_body = json.loads(req.body)
    # print(req_body)
    #
    # # Check req validity
    # res = {
    #     "error": "invalid request, please check the documentation for the correct request format"
    # }
    # # checking validity of post req body
    # try:
    #     valid_name = 'name' in req_body and type(req_body['name']) == str
    # except:
    #     return JsonResponse(res)
    #
    # # Return invalid request
    # if not valid_name:
    #     return JsonResponse(res)
    #
    # res = {'status': 'valid'}
    # res['data'] = []
    #
    # data = Strategy.objects.filter(
    #     name=req_body['name'],
    # )
    # res['data'] = StrategySerializer(data, many=True).data
    #
    # # if filtered data is empty
    # if not data:
    #     res = {
    #         'error': 'No data present in the db.'
    #     }
    #
    # return JsonResponse(res)


@api_view(['GET', ])
def api_get_orders(req):
    try:
        orders = Orders.objects.all()
        print("Orders:", orders)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(OrdersSerializer(orders, many=True).data)





