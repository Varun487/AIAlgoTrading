from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExampleBackTesterModel, BackTestReport, BackTestTrade
from .serializers import ExampleBackTesterSerializer, AllBacktestsSerializer, BacktestDataSerializer, \
    AllBacktestTradesSerializer, BacktestTradeDataSerializer

from services.Utils.getters import Getter

from strategies.models import StrategyType
from strategies.models import TickerData

from services.IndicatorCalc.indicators import BollingerIndicator
from services.SignalGeneration.bbsignalgeneration import BBSignalGenerator
from services.Visualizations.signal_visualization import SignalVisualization

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


def api_get_backtest_signal_visualization(req, backtest_id):

    backtest = BackTestReport.objects.get(id=backtest_id)

    df = Getter(table_name=TickerData, df_flag=True, param_list={'company': backtest.company,
                                                                 'time_stamp__range': [backtest.start_date_time,
                                                                                       backtest.end_date_time]}) \
        .get_data()

    df.drop(['id', 'company_id', 'time_period'], axis=1, inplace=True)

    df = BBSignalGenerator(
        indicator=BollingerIndicator(
            df=df,
            time_period=backtest.strategy_config.indicator_time_period,
            dimension=backtest.strategy_config.get_dimension_display(),
            sigma=backtest.strategy_config.sigma,
        )
    ).generate_signals()

    res = {
        "img": SignalVisualization(df=df, columns=list(df.columns), height=20, width=100).get_visualization()
    }

    return JsonResponse(res)
