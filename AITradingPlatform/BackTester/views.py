import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import ExampleBackTesterModel ,BackTestOrder, BackTestReport
from Strategies.models import Orders, Strategy
from DataFeeder.models import Company
from .serializers import ExampleBackTesterSerializer, BackTestReportSerializer, BackTestOrderSerializer
from datetime import datetime


@api_view(['GET', ])
def api_index(req, slug):
    print("Example Back Tester Model slug:", slug)

    try:
        name = ExampleBackTesterModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExampleBackTesterSerializer(name).data)


@api_view(['POST', ])
def api_get_orders(req):
    req_body = json.loads(req.body)
    print(req_body)
    # create response if request not valid
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # checking validity of post req body
    valid_order = 'order' in req_body and type(req_body['order']) == str
    valid_backtestreport = 'backtestreport' in req_body and type(req_body['backtestreport']) == str
    valid_company = 'company' in req_body and type(req_body['company']) == str
    valid_strategy = 'strategy' in req_body and type(req_body['strategy']) == str

    if not (valid_order and valid_backtestreport and valid_company and  valid_strategy):
        return JsonResponse(res)

    # check if correct date and time
    try:
        start_dt = datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S')
        end_dt = datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S')
    except:
        return JsonResponse(res)

    company_obj = Company.objects.get(ticker=req_body['company'])[0]
    # print( company_obj)
    strategy_obj = Strategy.objects.get(name=req_body['strategy'])[0]
    # print(strategy_obj)

    # res['backtestreport'] = BackTestReportSerializer(company_obj, strategy_obj)

    backtestreport_obj = BackTestReport.objects.filter(company=company_obj, strategy=strategy_obj)

    backtestorder_obj = BackTestOrder.objects.filter(order=req['order'], backtestreport=backtestreport_obj,
                                                     account_size=req['account_size'])

    res['backtestorder'] = BackTestReportSerializer(backtestorder_obj, many=True).data

    return JsonResponse(res)

