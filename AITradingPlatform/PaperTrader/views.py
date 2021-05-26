import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import ExamplePaperTraderModel, PaperTradedStrategies
from .serializers import ExamplePaperTraderSerializer, PaperTradedStrategiesSerializer


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
        res['Error'] = "No data in Data Base"

    res['Strategies'] = PaperTradedStrategiesSerializer(strategies_obj, many=True).data
    res['Listing_Status'] = "Sucess"

    return JsonResponse(res)