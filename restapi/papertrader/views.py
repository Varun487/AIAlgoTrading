from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from strategies.models import StrategyType

from backtester.models import BackTestReport

from .models import ExamplePaperTraderModel, PaperTrade, CurrentQuote

from .serializers import ExamplePaperTraderSerializer, AllPaperTradesSerializer, PaperTradeDataSerializer, \
    CompanyQuoteSerializer

from services.Visualizations.bb_visualizations.bb_paper_trade_visualization import BBPaperTradeVisualization
from services.Visualizations.lstm_visualizations.lstm_paper_trade_visualization import LSTMPaperTradeVisualization


@api_view(['GET', ])
def api_index(req, slug):
    print("Example PaperTrader Model slug:", slug)

    try:
        name = ExamplePaperTraderModel.objects.get(name=slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(ExamplePaperTraderSerializer(name).data)


@api_view(['GET', ])
def api_get_all_papertrades(req, strategy_type_id):
    try:
        strategy_type = StrategyType.objects.get(id=strategy_type_id)
        papertrades = PaperTrade.objects.filter(
            paper_traded_strategy__strategy_config__strategy_type=strategy_type
        ).order_by('-live')
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(AllPaperTradesSerializer(papertrades, many=True).data)


@api_view(['GET', ])
def api_get_papertrade_data(req, papertrade_id):
    try:
        papertrade = PaperTrade.objects.get(id=papertrade_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(PaperTradeDataSerializer(papertrade).data)


@api_view(['GET', ])
def api_get_company_quote(req, papertrade_id):
    try:
        current_quote = CurrentQuote.objects.get(
            company=PaperTrade.objects.get(id=papertrade_id).trade.entry_order.ticker_data.company
        )
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(CompanyQuoteSerializer(current_quote).data)


@api_view(['GET', ])
def api_get_paper_trade_visualization(req, papertrade_id):
    try:
        paper_trade = PaperTrade.objects.get(id=papertrade_id)
        # print(paper_trade)

        if paper_trade.paper_traded_strategy.strategy_config.strategy_type.name == "Simple Bollinger Band Strategy":
            visualization = BBPaperTradeVisualization
        else:
            visualization = LSTMPaperTradeVisualization

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
            "img": visualization(backtest_report=BackTestReport.objects.all()[0], paper_trade=paper_trade,
                                 height=height, width=width).get_visualization()
        }

        return JsonResponse(res)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
