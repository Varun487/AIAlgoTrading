import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import ExamplePaperTraderModel, PaperTradedStrategies, PaperTradeOrder
from .serializers import ExamplePaperTraderSerializer, PaperTradedStrategiesSerializer, PaperTradeOrderSerializer

from Strategies.models import Orders, Strategy
from Strategies.serializers import StrategySerializer, OrdersSerializer

@api_view(['GET', ])
def api_index(req, slug):
    print("Example Paper Trader Model slug:", slug)

    try:
        name = ExamplePaperTraderModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExamplePaperTraderSerializer(name).data)


@api_view(['GET', ])
def api_list_strategy(req):

    # create response if request not valid
    res = {'status': 'invalid request, please check the documentation for this request here'}

    strategies_obj = PaperTradedStrategies.objects.all()
    if not strategies_obj:
        return JsonResponse(res)


    res['Strategies'] = PaperTradedStrategiesSerializer(strategies_obj, many=True).data
    res['status'] = "Sucess"

    return JsonResponse(res)

@api_view(['POST', ])
def api_list_PaperTradeOrder(req):

    req_body = json.loads(req.body)
    # create response if request not valid
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # check the validity of req_body
    valid_strategy = 'strategy' in req_body and type(req_body['strategy']) == str
    valid_live_order = 'live_order' in req_body and type(req_body['live_order']) == bool


    if not (valid_strategy and valid_live_order):
        res = {'status': 'Invalid request body'}
        return JsonResponse(res)


    strategy_obj = PaperTradedStrategies.objects.get(name=req_body['strategy'])
    print(strategy_obj)

    res = {'status': 'valid'}
    res['data'] = []


    # filter data for request
    data = PaperTradeOrder.objects.filter(
        strategy = strategy_obj,
        live_order = req_body['live_order'],
    )
    res['data'] = PaperTradeOrderSerializer(data, many=True).data

    # if filtered data is empty
    if not data:
        res = {
            'error': 'No data present that fits all conditions. Please try sourcing the data or computing indicators.'
        }

    return JsonResponse(res)


