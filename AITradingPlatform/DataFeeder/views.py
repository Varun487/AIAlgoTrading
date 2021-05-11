from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ExampleDataFeederModel, Company
from .serializers import ExampleDataFeederSerializer, ListCompaniesSerializer

# REST Api Views

@api_view(['GET', ])
def api_index(req, slug):
    print("Example Data Feeder Model slug:", slug)

    try:
        name = ExampleDataFeederModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExampleDataFeederSerializer(name).data)


@api_view(['GET', ])
def api_list_companies(req):

    try:
        companies = Company.objects.all()
        print("Companies: ", companies)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ListCompaniesSerializer(companies, many=True).data)

