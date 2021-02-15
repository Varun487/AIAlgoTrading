from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ExampleBackTesterModel
from .serializers import ExampleBackTesterSerializer


@api_view(['GET', ])
def api_index(req, slug):
    print("slug:", slug)

    try:
        name = ExampleBackTesterModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExampleBackTesterSerializer(name).data)
