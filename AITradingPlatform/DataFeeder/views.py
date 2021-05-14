import pandas as pd
from django.http import JsonResponse

from datetime import datetime
import json
import pandas_datareader.data as web

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ExampleDataFeederModel, Company, ImmutableData
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


@api_view(['POST', ])
def api_get_data_on_demand(req):
    # Get the request
    req_body = json.loads(req.body)
    print("req_body: ", req_body)

    # creating default response
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # checking validity of post req body
    valid_companies = 'companies' in req_body and type(req_body['companies']) == list
    valid_provider = 'provider' in req_body and req_body['provider'] in ['Yahoo', 'Alpha']
    valid_time_period = 'time_period' in req_body and req_body['time_period'] in ['daily', '60min', '30min', '15min',
                                                                                  '10min', '5min', '1min']

    # check if correct date and time
    try:
        start_dt = datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S')
        end_dt = datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S')
    except:
        return JsonResponse(res)

    # Return invalid request
    if not (valid_companies and valid_provider and valid_time_period):
        return JsonResponse(res)

    # create response
    res['status'] = 'valid'
    res['collected_data'] = []
    res['data_not_found'] = []
    res['provider'] = req_body['provider']

    # collect data per company
    for company in req_body['companies']:

        try:
            # company must exist in DB to collect data
            company_obj = Company.objects.get(ticker=company)

            # collect yahoo finance data
            if req_body['provider'] == 'Yahoo':

                # collect data
                df = web.DataReader(f"{company}", 'yahoo', start_dt, end_dt)

            # collect AlphaVantage data
            else:
                print(f'Alpha {company}')

            # Process dataframe to send to DB
            for i in range(len(df)):

                # Put collected data in DB if not already present
                if not ImmutableData.objects.all().filter(company=company_obj, time_stamp=df.index[i]):
                    ImmutableData(
                        time_stamp=df.index[i],
                        company=company_obj,
                        open=df.Open[i],
                        high=df.High[i],
                        low=df.Low[i],
                        close=df.Close[i],
                        volume=df.Volume[i],
                        time_period='daily',
                    ).save()
                else:
                    print(f'data already exists for {company} at {df.index[i]}')

            res['collected_data'].append(company)

        except:
            res['data_not_found'].append(company)

    return JsonResponse(res)
