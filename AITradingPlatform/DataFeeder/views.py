from django.http import JsonResponse

from datetime import datetime
import json

from django.utils.timezone import make_aware
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ExampleDataFeederModel, Company
from .serializers import ExampleDataFeederSerializer, ListCompaniesSerializer

from .utils import get_data_on_demand


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


@api_view(['POST', ])
def api_get_data_on_demand(req):
    # Get the request
    req_body = json.loads(req.body)
    # print("req_body: ", req_body)

    # creating default response
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # list of allowed slices
    allowed_slices = [f'year{year}month{month}' for year in range(1, 3) for month in range(1, 13)]

    # checking validity of post req body
    valid_companies = 'companies' in req_body and type(req_body['companies']) == list
    valid_provider = 'provider' in req_body and req_body['provider'] in ['Yahoo', 'Alpha']
    valid_time_period = 'time_period' in req_body and req_body['time_period'] in ['daily', '60min', '30min', '15min',
                                                                                  '10min', '5min', '1min']
    valid_slice = 'slice' in req_body and req_body['slice'] in allowed_slices

    # check if correct date and time
    try:
        start_dt = make_aware(datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S'))
        end_dt = make_aware(datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S'))
    except:
        return JsonResponse(res)

    # Return invalid request
    if not (valid_companies and valid_provider and valid_time_period and valid_slice):
        return JsonResponse(res)

    # create response
    res['status'] = 'valid'
    res['collected_data'] = []
    res['data_not_found'] = []
    res['provider'] = req_body['provider']

    # Get data on demand
    res['collected_data'], res['data_not_found'] = get_data_on_demand(req_body['companies'], req_body['provider'],
                                                                      start_dt, end_dt, req_body['time_period'],
                                                                      req_body['slice'])

    return JsonResponse(res)
