import json
import sys
from datetime import datetime
from os import environ

import pandas as pd
import pandas_datareader.data as web
from django.db.models import Max, Min, Sum
from django.http import JsonResponse
from django.utils.timezone import make_aware
from pandas_datareader._utils import RemoteDataError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExampleDataFeederModel, Company, ImmutableData, Indicators, CalculatedCandleStick
from .serializers import ExampleDataFeederSerializer, ListCompaniesSerializer, IndicatorsSerializer, CandleStickSerializer, ImmutableDataSerializer

from .utils import calc_indicators, push_indicators_to_db
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
def api_company_details(req):
    req_body = json.loads(req.body)

    # creating default response
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # validate request parameters
    valid_company = 'company' in req_body and type(req_body['company']) == str

    # check request validity
    if not valid_company:
        return JsonResponse(res)
    print(res)
    # verify whether company exits in db
    try:
        company_obj = Company.objects.get(ticker=req_body['company'])  # name or ticker
        res = {'status': 'valid'}
        res['company'] = ListCompaniesSerializer(company_obj).data  # line can be commented
        res['data'] = []

        # filter data for request
        data = Company.objects.filter(ticker=company_obj)
        res['data'] = ListCompaniesSerializer(data, many=True).data

    except Company.DoesNotExist:
        res = {'error': 'No such data present. Please enter a valid company name.'}
        return JsonResponse(res)

    return JsonResponse(res)


@api_view(['POST', ])
def api_filter_company(req):
    req_body = json.loads(req.body)

    # creating default response
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # validate request parameters
    valid_sector = 'sector' in req_body and type(req_body['sector']) == str

    # check request validity
    if not (valid_sector):
        return JsonResponse(res)

    if 'sector' in req_body:
        try:
            company_obj = Company.objects.filter(sector=req_body['sector'])
            print(company_obj)
            res = {'status': 'valid'}
            res['data'] = ListCompaniesSerializer(company_obj,many=True).data
        except:
            res = {'status': 'invalid'}

    return JsonResponse(res)



@api_view(['POST', ])
def api_add_company(req):
    req_body = json.loads(req.body)

    # creating default response
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # validate post request parameters
    valid_name = 'name' in req_body and type(req_body['name']) == str
    valid_sector = 'sector' in req_body and type(req_body['sector']) == str
    valid_ticker = 'ticker' in req_body and type(req_body['ticker']) == str

    # check request validity
    if not (valid_name and valid_sector and valid_ticker):
        return JsonResponse(res)

    # verify if company already exists in DB
    if not Company.objects.filter(name=req_body['name'], sector=req_body['sector'], ticker=req_body['ticker']):
        Company(
            name=req_body['name'],
            sector=req_body['sector'],
            ticker=req_body['ticker'],
        ).save()
        res = {'status': 'Valid request. Company added successfully.'}
        return JsonResponse(res)
    else:
        res = {'status': 'Invalid request. Company already exists in Database.'}
        return JsonResponse(res)


@api_view(['POST', ])
def api_delete_company(req):
    req_body = json.loads(req.body)

    # creating default response
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # validate request parameters
    valid_company = 'company' in req_body and type(req_body['company']) == str

    # check request validity
    if not valid_company:
        return JsonResponse(res)


    res['data_deleted'] = []
    try:
        company_obj = Company.objects.get(ticker=req_body['company'])
        res['data'] = company_obj
        company_obj.delete()
        res = {'status': 'valid'}
        res = {'data_deleted': 'success'}
    except:
        res = {'data_deleted': 'fail'}
        res = {'error': 'No such data present. Please enter a valid company ticker.'}

    return JsonResponse(res)


@api_view(['POST', ])
def api_modify_company_attr(req):
    req_body = json.loads(req.body)

    # creating default response
    res = {'status': 'invalid request, please check the documentation for this request here'}


    # validate post request parameters
    valid_n = "name" in req_body and type(req_body['name']) == str
    valid_name = 'new_name' in req_body and type(req_body['new_name']) == str
    valid_sector = 'new_sector' in req_body and type(req_body['new_sector']) == str
    valid_ticker = 'new_ticker' in req_body and type(req_body['new_ticker']) == str

    # check request validity
    if not (valid_name and valid_sector and valid_ticker and valid_n):
        return JsonResponse(res)

    # verify if company exists
    try:
        company_obj = Company.objects.filter(name=req_body['name'])
        new_name = req_body['new_name']
        new_sector = req_body['new_sector']
        new_ticker = req_body['new_ticker']
        print(company_obj)
        # check for modification and update model object
        if 'new_name' in req_body:
            company_obj.update(name=new_name)
        if 'new_sector' in req_body:
            company_obj.update(sector=new_sector)
        if 'new_ticker' in req_body:
            company_obj.update(ticker=new_ticker)

        res = {'status': 'valid'}
        res = {'update': 'success'}
        #res['data'] = ListCompaniesSerializer(company_obj).data
    except:
        res = {'status': 'invalid'}
        res = {'update': 'fail'}
        res = {'data':'Invalid request. Company does not exist in Database.'}

    return JsonResponse(res)



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


@api_view(['POST', ])
def api_calcderievedindiactor(req):

    allowed_slices = [f'year{year}month{month}' for year in range(1, 3) for month in range(1, 13)]
    req_body = json.loads(req.body)
    # print("req_body: ", req_body)
    # creating default response
    res = {'status': 'invalid request, please check the documentation for this request here'}
    # print(req_body)

    # checking validity of post req body

    valid_companies = 'company' in req_body and type(req_body['company']) == str
    valid_provider ='provider' in req_body and type(req_body['provider'])==str
    valid_time_period = 'time_period' in req_body and req_body['time_period'] in ['daily', '60min', '30min', '15min',
                                                                                '10min', '5min', '1min']

    valid_slice = 'slice' in req_body and req_body['slice'] in allowed_slices
    valid_column = 'column' in req_body and req_body['column'] in ['Open', 'High', 'Low', 'Close', 'Volume']
    valid_indicator_time_period = 'indicator_time_period' in req_body and type(req_body['indicator_time_period']) == int
    valid_name='name' in req_body and req_body['name'] in ['SMA','Std_Dev','BB_down','BB_up']

    if not (valid_name and valid_slice and valid_column and valid_companies and valid_indicator_time_period and valid_provider):
        return JsonResponse(res)

    res['validation_status'] ="sucess"

    # getting data into database

    res['status'] = "sucess"
    start_dt = make_aware(datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S'))
    end_dt = make_aware(datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S'))
    res['collected_data'], res['data_not_found'] = get_data_on_demand([req_body['company']], req_body['provider'],
                                                                      start_dt, end_dt, req_body['time_period'],
                                                                      req_body['slice'])
    # retrieval of data from database

    company_obj = Company.objects.filter(ticker=req_body['company'])[0]
    data = ImmutableData.objects.filter(company=company_obj, time_period=req_body['time_period'],
                                              time_stamp__range=[start_dt,end_dt])
    # data1 = ImmutableData.objects.all().filter(company=company_obj, time_period=req_body['time_period'],
    #                                           time_stamp=req_body['time_stamp'])[0]
    # print(data1)
    res['retrieval_status'] = "sucess"

    # converting into dataframe

    time_stamp =[]
    column = []

    for candlestick in data:
        print(candlestick.time_stamp, eval(f"candlestick.{req_body['column'].lower()}"))
        time_stamp.append(candlestick.time_stamp)
        column.append(eval(f"candlestick.{req_body['column'].lower()}"))
    df = pd.DataFrame(columns=["time_stamp", req_body['column']])
    df['time_stamp']= time_stamp
    df[req_body['column']]= column


    res['convert_dataframe_status'] = "sucess"



    # calculating indicators

    df = calc_indicators(df, req_body['indicator_time_period'], req_body['column'])
    df.set_index('time_stamp',inplace=True)
    df.dropna(inplace=True)
    print(df)

    res['calculated_indicators_status'] = "sucess"


    # pushing to database

    push_indicators_to_db(df, f'{req_body["name"]}_{req_body["column"]}_{req_body["indicator_time_period"]}',
                          company_obj,req_body["indicator_time_period"], req_body['time_period'], req_body["column"])

    res['pushed_status'] = "sucess"


    return JsonResponse(res)
    
@api_view(['POST', ])
def api_derive_candle_stick(req):

    req_body = json.loads(req.body)
    print(req_body)
    # create response if request not valid
    res = {'status': 'invalid request, please check the documentation for this request here'}

    #check the validity of req_body
    valid_company = 'company' in req_body and type(req_body['company']) == str
    valid_calculate_time_period = 'calculate_time_period' in req_body and type(req_body['calculate_time_period']) == int
    valid_original_time_period = 'original_time_period' in req_body and req_body['original_time_period'] in ['daily','60min',
                                                                                                          '30min',
                                                                                                          '15min',
                                                                                                          '10min',
                                                                                                          '5min',
                                                                                                          '1min']
    valid_provider = 'provider' in req_body and req_body['provider'] in ['Yahoo', 'Alpha']
    if not (valid_company and valid_calculate_time_period and valid_original_time_period and valid_provider):
        res = {'status': 'Invalid request body'}
        return JsonResponse(res)

    # check if correct date and time

    try:
        start_dt = make_aware(datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S'))
        end_dt = make_aware(datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S'))
    except:
        	
        res ={'status': 'Invalid Start date and end date'}
        return JsonResponse(res)

    company_obj = Company.objects.get(ticker=req_body['company'])
    collected_data, data_not_found = get_data_on_demand([req_body['company']], req_body['provider'], start_dt, end_dt, req_body['original_time_period'], req_body['slice'])

    #data = ImmutableData.objects.filter(company=company_obj, time_stamp__range=[start_dt,end_dt], time_period=req_body['original_time_period'])
    data = ImmutableData.objects.order_by('time_stamp').filter(company=company_obj, time_stamp__range=[start_dt,end_dt], time_period=req_body['original_time_period'])
    print(collected_data,data_not_found)
    try:
        n = req_body['calculate_time_period']
        items_remove = data.count() % n
        print(items_remove)
        data = data.all()[:data.count()-items_remove]
        print(data.count())
        open = []
        close = []
        high = []
        low = []
        volume = []
        date_of_candlestick = []
        for i in range(0, data.count(), n):
            data1 = data.all()[i:n+i]
            open.append(data1.values('open')[0])
            close.append(data1.values('close')[data1.count()-1])
            high.append(data1.aggregate(Max('high')))
            low.append(data1.aggregate(Min('low')))
            volume.append(data1.aggregate(Sum('volume')))
            date_of_candlestick.append(data1.values('time_stamp')[data1.count()-1])


        open1 = []
        close1 = []
        high1 = []
        low1 = []
        volume1 = []
        date_of_candlestick1 = []

        for i in range(len(open)):
            for j in open[i].values():
                open1.append(j)
            for j in close[i].values():
                close1.append(j)
            for j in high[i].values():
                high1.append(j)
            for j in low[i].values():
                low1.append(j)
            for j in volume[i].values():
                volume1.append(j)
            for j in date_of_candlestick[i].values():
                date_of_candlestick1.append(j)
        #rint(date_of_candlestick1)
        # print(open1,close1,low1,high1,volume1)
        for i in range(len(open1)):

            # Put collected data in DB if not already present
            if not CalculatedCandleStick.objects.all().filter(company=company_obj, time_stamp__range=[start_dt,end_dt], time_period=req_body['original_time_period']+'_'+str(req_body['calculate_time_period'])):
                CalculatedCandleStick(
                    company=company_obj,
                    open=open1[i],
                    high=high1[i],
                    low=low1[i],
                    close=close1[i],
                    volume=volume1[i],
                    time_period=req_body['original_time_period']+'_'+str(req_body['calculate_time_period']),
                    time_stamp=date_of_candlestick1[i],
                ).save()

    except Exception as e:

        print("Exception occured: ", e)

        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)
        res = {'status': 'Not Enough data'}
        return JsonResponse(res)
    res={'status':'Candle Sticks have been derived'}
    return JsonResponse(res)

@api_view(['POST', ])
def api_get_candlestick_data(req):

    req_body = json.loads(req.body)
    print(req_body)
    # create response if request not valid
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # check the validity of req_body
    valid_company = 'company' in req_body and type(req_body['company']) == str
    valid_calculate_time_period = 'calculate_time_period' in req_body and type(req_body['calculate_time_period']) == int
    valid_original_time_period = 'original_time_period' in req_body and req_body['original_time_period'] in ['daily','60min',
                                                                                                          '30min',
                                                                                                          '15min',
                                                                                                          '10min',
                                                                                                          '5min',
                                                                                                          '1min']
    valid_provider = 'provider' in req_body and req_body['provider'] in ['Yahoo', 'Alpha']

    if not (valid_company and valid_calculate_time_period and valid_original_time_period and valid_provider):
        res = {'status': 'Invalid request body'}
        return JsonResponse(res)

    # check if correct date and time
    try:
        start_dt = make_aware(datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S'))
        end_dt = make_aware(datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S'))
    except:
        return JsonResponse(res)

    company_obj = Company.objects.get(ticker=req_body['company'])


    res = {'status': 'valid'}
    res['company'] = ListCompaniesSerializer(company_obj).data
    res['data'] = []

    # filter data for request
    data = CalculatedCandleStick.objects.filter(
        company=company_obj,
        time_period = req_body['original_time_period']+'_'+str(req_body['calculate_time_period']),
        time_stamp__range=[start_dt, end_dt],
    )

    res['data'] = CandleStickSerializer(data, many=True).data

    # if filtered data is empty
    if not data:
        res = {
            'error': 'No data present that fits all conditions. Please try sourcing the data or computing indicators.'
        }

    return JsonResponse(res)


@api_view(['POST', ])
def api_listimmutable(req):

    req_body = json.loads(req.body)
    print(req_body)
    # create response if request not valid
    res = {'status': 'invalid request, please check the documentation for this request here'}

    # checking validity of post req body

    valid_company = 'company' in req_body and type(req_body['company']) == str
    valid_time_period = 'time_period' in req_body and req_body['time_period'] in ['daily', '60min', '30min', '15min',
                                                                                  '10min', '5min', '1min']
    if not (valid_company and valid_time_period):
        res = {'status': 'Invalid request body'}
        return JsonResponse(res)

    res['validation_status']="sucess"

    # filtering immutable data according to parameters

    start_dt = make_aware(datetime.strptime(req_body['start_date'], '%Y-%m-%d %H:%M:%S'))
    end_dt = make_aware(datetime.strptime(req_body['end_date'], '%Y-%m-%d %H:%M:%S'))
    company_obj = Company.objects.filter(ticker=req_body['company'])[0]

    #res['company'] = ListCompaniesSerializer(company_obj).data

    immutable = ImmutableData.objects.all().filter(company=company_obj,time_period=req_body['time_period'],time_stamp__range=[start_dt,end_dt])
    print(immutable)

    res['immutable'] = ImmutableDataSerializer(immutable, many=True).data

    res['filtering status'] = "sucess"



    return JsonResponse(res)


