from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExampleStrategiesModel, StrategyType
from .serializers import ExampleStrategiesSerializer, AllStrategiesStrategyTypeSerializer, \
    StrategyDataStrategyTypeSerializer


@api_view(['GET', ])
def api_index(req, slug):
    print("Example strategies Model slug:", slug)

    try:
        name = ExampleStrategiesModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExampleStrategiesSerializer(name).data)


@api_view(['GET', ])
def api_get_all_strategies(req):
    try:
        strategies = StrategyType.objects.all()
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(AllStrategiesStrategyTypeSerializer(strategies, many=True).data)


@api_view(['GET', ])
def api_get_strategy_data(req, strategy_id):

    try:
        strategies = StrategyType.objects.get(id=strategy_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(StrategyDataStrategyTypeSerializer(strategies).data)
