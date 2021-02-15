from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ExamplePaperTraderModel
from .serializers import ExamplePaperTraderSerializer


@api_view(['GET', ])
def api_index(req, slug):
    print("slug:", slug)

    try:
        name = ExamplePaperTraderModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExamplePaperTraderSerializer(name).data)
