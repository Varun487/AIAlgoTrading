from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExampleStrategiesModel, StrategyType, Company, TickerData
from .serializers import ExampleStrategiesSerializer, AllStrategiesStrategyTypeSerializer, \
    StrategyDataStrategyTypeSerializer

from services.Utils.getters import Getter
from services.SourceData.sourcedata import SourceData
import datetime
from django.utils.timezone import make_aware


def source_and_store():
    # Source all company data and put in storage folder
    all_companies = list(Company.objects.all())

    for company in all_companies:
        df = SourceData(
            company=company,
            start_date=datetime.datetime(2017, 1, 1),
            end_date=datetime.datetime(2020, 12, 31),
        ).get_df()
        df.reset_index(inplace=True)
        df.rename(
            columns={'Close': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low', 'Date': 'time_stamp',
                     'Volume': 'volume'},
            inplace=True
        )
        df['time_stamp'] = [make_aware(time_stamp) for time_stamp in df['time_stamp']]
        df.to_csv(f'/home/app/restapi/Storage/{company.ticker}.csv', index=False)


@api_view(['GET', ])
def api_index(req, slug):
    print("Example strategies Model slug:", slug)

    try:
        # source_and_store()
        name = ExampleStrategiesModel.objects.get(name=slug)

    except Exception as e:
        print(e)
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
