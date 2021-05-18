import pandas as pd
from django.http import JsonResponse

from datetime import datetime
from datetime import timedelta
import json
import pandas_datareader.data as web
from os import environ

from django.utils.timezone import make_aware
from pandas_datareader._utils import RemoteDataError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ExampleDataFeederModel, Company, ImmutableData, Indicators
from .serializers import ExampleDataFeederSerializer, ListCompaniesSerializer, IndicatorsSerializer


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
        start_dt = datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S')
        end_dt = datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S')
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

                url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={company}&interval={req_body["time_period"]}&slice={req_body["slice"]}&adjusted=false&apikey={environ["API_KEY"]}'

                df = pd.read_csv(url)
                df['time'] = pd.to_datetime(df['time'])

                df = df[start_dt <= df.time]
                df = df[df.time <= end_dt]
                df.set_index('time', inplace=True)

                for col in df.columns:
                    df.rename(columns={col: col.capitalize()}, inplace=True)

            # Process dataframe to send to DB
            for i in range(len(df)):

                # Put collected data in DB if not already present
                if not ImmutableData.objects.all().filter(company=company_obj, time_stamp=df.index[i],
                                                          time_period=req_body["time_period"]):
                    ImmutableData(
                        time_stamp=df.index[i],
                        company=company_obj,
                        open=df.Open[i],
                        high=df.High[i],
                        low=df.Low[i],
                        close=df.Close[i],
                        volume=df.Volume[i],
                        time_period=req_body['time_period'],
                    ).save()

            res['collected_data'].append(company)

        except RemoteDataError:
            res['data_not_found'].append(company)

    # except:
    # 	res['data_not_found'].append(company)

    return JsonResponse(res)

@api_view(['POST', ])
def api_get_indicators_data(req):
    # Get the request
    req_body = json.loads(req.body)

    # create response if request not valid
    res = {'error': 'Invalid request. Please check the parameters.'}

    # check if correct date and time
    try:
        start_dt = make_aware(datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S'))
        end_dt = make_aware(datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S'))
    except:
        return JsonResponse(res)

    # validate request parameters
    valid_name = 'name' in req_body and type(req_body['name']) == str
    valid_company = 'company' in req_body and type(req_body['company']) == str
    valid_candle_stick_period = 'candle_stick_period' in req_body and req_body['candle_stick_period'] in ['daily',
                                                                                                          '60min',
                                                                                                          '30min',
                                                                                                          '15min',
                                                                                                          '10min',
                                                                                                          '5min',
                                                                                                          '1min']
    valid_indicator_time_period = 'indicator_time_period' in req_body and type(req_body['indicator_time_period']) == int
    valid_column = 'column' in req_body and req_body['column'] in ['Open', 'High', 'Low', 'Close', 'Volume']
    valid_lower_value = 'value_range_lower' in req_body and type(req_body['value_range_lower']) == int
    valid_higher_value = 'value_range_higher' in req_body and type(req_body['value_range_higher']) == int

    valid_request = valid_company and valid_candle_stick_period and valid_indicator_time_period and valid_column and \
                    valid_name and valid_lower_value and valid_higher_value

    # Check request validity
    if not valid_request:
        return JsonResponse(res)

    company_obj = Company.objects.all().filter(ticker=req_body['company'])[0]

    res = {'status': 'valid'}
    res['indicator'] = req_body['name']
    res['company'] = ListCompaniesSerializer(company_obj).data
    res['data'] = []

    # filter data for request
    data = Indicators.objects.filter(
        name=req_body['name'],
        column=req_body['column'],
        indicator_time_period=req_body['indicator_time_period'],
        candle_stick__company=company_obj.id,
        candle_stick__time_period=req_body['candle_stick_period'],
        value__range=[req_body['value_range_lower'], req_body['value_range_higher']],
        candle_stick__time_stamp__range=[start_dt, end_dt],
    )

    res['data'] = IndicatorsSerializer(data, many=True).data

    # if filtered data is empty
    if not data:
        res = {
            'error': 'No data present that fits all conditions. Please try sourcing the data or computing indicators.'
        }

    return JsonResponse(res)


@api_view(['GET', ])
def calcderievedindiactor(req):
    data = ImmutableData.objects.all()
    df = pd.read_csv(data)



@api_view(['POST', ])
def api_derive_candle_stick(req):
	
	req_body = json.loads(req.body)

	companies = 'companies' in req_body and type(req_body['companies']) == list
	time_period = 'time_period' in req_body and req_body['time_period'] in ['daily', '60min', '30min', '15min', '10min', '5min', '1min']

	try:
        start_dt = make_aware(datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S'))
        end_dt = make_aware(datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S'))
    except:
        return JsonResponse(res)
	
	company_obj = Company.objects.get(ticker=company)

	#for i in ImmutableData.objects.all().filter(company=company_obj, time_stamp=start_dt):
		#if time_period !=time:
			 

	days = (end_dt - start_dt).days

	def get_date(n):
		return datetime.strftime(start_dt + timedelta(days=n), '%Y-%m-%d %H:%M:%S')
	
    
	for n in range(0, days, time_period):
        
		yield get_date(n)