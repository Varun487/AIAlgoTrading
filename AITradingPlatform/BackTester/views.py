import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ExampleBackTesterModel
from .serializers import ExampleBackTesterSerializer
from Strategies.utils import simple_bollinger_bands_strategy

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

    try:
        start_dt = make_aware(datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S'))
        end_dt = make_aware(datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S'))
        valid_max_risk = type(req['max_risk']) == float
        valid_initial_acc = type(req['initial_acc']) == float
        valid_company = type(req_body['company']) == str
        # valid_strategy = type(req_body['strategy']) == str
    except:

        res = {'status': 'Invalid Start date and end date'}
        return JsonResponse(res)

    simple_bollinger_bands_strategy()

