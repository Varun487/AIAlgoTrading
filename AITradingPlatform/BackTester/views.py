import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import ExampleBackTesterModel
from .serializers import ExampleBackTesterSerializer


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


    return JsonResponse(res)

