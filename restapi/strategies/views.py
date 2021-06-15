from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExampleStrategiesModel
from .serializers import ExampleStrategiesSerializer


@api_view(['GET', ])
def api_index(req, slug):
    print("Example strategies Model slug:", slug)

    try:
        name = ExampleStrategiesModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExampleStrategiesSerializer(name).data)
