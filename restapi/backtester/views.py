from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExampleBackTesterModel, BackTestTrade, BackTestReport
from .serializers import ExampleBackTesterSerializer, BackTestTradeSerializer, BackTestReportSerializer


@api_view(['GET', ])
def api_index(req, slug):
    print("Example Back Tester Model slug:", slug)

    try:
        name = ExampleBackTesterModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExampleBackTesterSerializer(name).data)


@api_view(['GET', ])
def api_listbacktests(req):
    try:
        backtest = BackTestTrade.objects.all()
        print("Backtests:", backtest)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(BackTestTradeSerializer(backtest, many=True).data)


@api_view(['GET', ])
def api_listreports(req, id):
    try:
        reports = BackTestReport.objects.get(reports=id)
        print("reportdata:", reports)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(BackTestReportSerializer(reports, many=True).data)
