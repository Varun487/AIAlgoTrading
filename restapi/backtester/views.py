from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from services.Visualizations.bb_visualizations.bb_signal_visualization import BBSignalVisualization
from services.Visualizations.bb_visualizations.bb_trade_visualization import BBTradeVisualization
from strategies.models import StrategyType

from .models import ExampleBackTesterModel, BackTestReport, BackTestTrade
from .serializers import ExampleBackTesterSerializer, AllBacktestsSerializer, BacktestDataSerializer, \
    AllBacktestTradesSerializer, BacktestTradeDataSerializer


@api_view(['GET', ])
def api_index(req, slug):
    print("Example Back Tester Model slug:", slug)

    try:
        name = ExampleBackTesterModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExampleBackTesterSerializer(name).data)


@api_view(['GET', ])
def api_get_all_backtests(req, strategy_type_id):
    try:
        strategy_type = StrategyType.objects.get(id=strategy_type_id)
        backtests = BackTestReport.objects.filter(strategy_type=strategy_type)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(AllBacktestsSerializer(backtests, many=True).data)


@api_view(['GET', ])
def api_get_backtest_data(req, backtest_id):
    try:
        backtest = BackTestReport.objects.get(id=backtest_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(BacktestDataSerializer(backtest).data)


@api_view(['GET', ])
def api_get_all_backtest_trades(req, backtest_id):
    try:
        backtest_trades = BackTestTrade.objects.filter(back_test_report__id=backtest_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(AllBacktestTradesSerializer(backtest_trades, many=True).data)


@api_view(['GET', ])
def api_get_backtest_trade_data(req, backtest_trade_id):
    try:
        backtest_trades = BackTestTrade.objects.get(id=backtest_trade_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(BacktestTradeDataSerializer(backtest_trades).data)


@api_view(['GET', ])
def api_get_backtest_signal_visualization(req, backtest_id):
    try:
        backtest_report = BackTestReport.objects.get(id=backtest_id)

        visualization = None

        if backtest_report.strategy_type.name == "Simple Bollinger Band Strategy":
            visualization = BBSignalVisualization

        # set height if present
        try:
            height = int(req.GET['height'])
        except:
            height = 20

        # set width if present
        try:
            width = int(req.GET['width'])
        except:
            width = 100

        res = {
            "img": visualization(backtest_report=backtest_report, height=height, width=width).get_visualization()
        }

        return JsonResponse(res)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', ])
def api_get_backtest_trade_visualization(req, backtest_trade_id):
    try:
        bt_trade = BackTestTrade.objects.get(id=backtest_trade_id)

        visualization = None

        if bt_trade.back_test_report.strategy_type.name == "Simple Bollinger Band Strategy":
            visualization = BBTradeVisualization

        # set height if present
        try:
            height = int(req.GET['height'])
        except:
            height = 6

        # set width if present
        try:
            width = int(req.GET['width'])
        except:
            width = 15

        res = {
            "img": visualization(backtest_report=bt_trade.back_test_report, backtest_trade=bt_trade,
                                 height=height,
                                 width=width).get_visualization()
        }

        return JsonResponse(res)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
