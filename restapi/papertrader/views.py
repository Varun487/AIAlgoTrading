from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExamplePaperTraderModel
from .serializers import ExamplePaperTraderSerializer


# Example
@api_view(['GET', ])
def api_index(req, slug):
    print("Example PaperTrader Model slug:", slug)

    try:
        name = ExamplePaperTraderModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExamplePaperTraderSerializer(name).data)
