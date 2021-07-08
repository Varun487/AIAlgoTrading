from rest_framework import serializers
from .models import ExamplePaperTraderModel, PaperTrade, CurrentQuote


class ExamplePaperTraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamplePaperTraderModel
        fields = ['name']


class AllPaperTradesSerializer(serializers.ModelSerializer):
    company_ticker = serializers.CharField(source='trade.entry_order.ticker_data.company.ticker')
    return_percent = serializers.FloatField(source='trade.return_percent')

    class Meta:
        model = PaperTrade
        fields = ['id', 'company_ticker', 'return_percent', 'live']
        depth = 2


class PaperTradeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperTrade
        fields = ['id', 'trade', 'paper_traded_strategy', 'live', 'take_profit', 'stop_loss']
        depth = 2


class CompanyQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentQuote
        fields = ['id', 'company', 'ticker_data', 'last_updated']
        depth = 1
