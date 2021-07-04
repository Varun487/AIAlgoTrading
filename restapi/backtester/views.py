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
from services.Visualizations.trade_visualization import TradeVisualization

from services.OrderExecution.calctakeprofitstoploss import TakeProfitAndStopLossBB
from services.OrderExecution.orderexecution import OrderExecution
from services.TradeEvaluation.tradeevaluator import TradeEvaluator


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
            "img": SignalVisualization(backtest_report=backtest_report, height=height, width=width).get_visualization()
        }

        return JsonResponse(res)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', ])
def api_get_backtest_trade_visualization(req, backtest_trade_id):
    try:
        bt_trade = BackTestTrade.objects.get(id=backtest_trade_id)

        trade_number = list(BackTestTrade.objects.filter(back_test_report=bt_trade.back_test_report)).index(
            bt_trade) + 1

        df = Getter(table_name=TickerData, df_flag=True, param_list={'company': bt_trade.back_test_report.company,
                                                                     'time_stamp__range': [
                                                                         bt_trade.back_test_report.start_date_time,
                                                                         bt_trade.back_test_report.end_date_time
                                                                     ]}).get_data()

        df.drop(['id', 'company_id', 'time_period'], axis=1, inplace=True)

        df = BBSignalGenerator(
            indicator=BollingerIndicator(
                df=df,
                time_period=bt_trade.back_test_report.strategy_config.indicator_time_period,
                dimension=bt_trade.back_test_report.strategy_config.get_dimension_display(),
                sigma=bt_trade.back_test_report.strategy_config.sigma,
            )
        ).generate_signals()

        # Add take profit and stop loss price
        df = TakeProfitAndStopLossBB(df=df, dimension=bt_trade.back_test_report.strategy_config.get_dimension_display(),
                                     factor=bt_trade.back_test_report.strategy_config.take_profit_factor).get_calc_df()

        # Execute orders
        df = OrderExecution(df=df, max_holding_period=bt_trade.back_test_report.strategy_config.max_holding_period,
                            dimension=bt_trade.back_test_report.strategy_config.get_dimension_display()).execute()

        # Evaluate trades
        df = TradeEvaluator(df=df).get_evaluated_df()

        res = {
            "img": TradeVisualization(df=df, columns=list(df.columns), height=6, width=15, trade_number=trade_number)
                .get_visualization()
        }

        return JsonResponse(res)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
