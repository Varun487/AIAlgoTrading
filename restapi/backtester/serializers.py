from rest_framework import serializers
from .models import ExampleBackTesterModel, BackTestTrade, BackTestReport


class ExampleBackTesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleBackTesterModel
        fields = ['name']


class AllBacktestsSerializer(serializers.ModelSerializer):
    company_ticker = serializers.CharField(source='company.ticker')

    class Meta:
        model = BackTestReport
        fields = ['id', 'company_ticker', 'total_returns', 'total_returns_percent']


class BacktestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackTestReport
        fields = ['id', 'start_date_time', 'end_date_time', 'strategy_type', 'strategy_config', 'total_returns',
                  'total_returns_percent', 'total_trades', 'profit_trades', 'profit_trades_percent', 'company']
        depth = 1


class AllBacktestTradesSerializer(serializers.ModelSerializer):
    trade_type = serializers.CharField(source='trade.entry_order.signal.type')
    trade_net_return = serializers.FloatField(source='trade.net_return')
    trade_return_percent = serializers.FloatField(source='trade.return_percent')
    trade_id = serializers.IntegerField(source='trade.id')

    class Meta:
        model = BackTestTrade
        fields = ['id', 'trade_id', 'trade_type', 'trade_net_return', 'trade_return_percent']


class BacktestTradeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackTestTrade
        fields = ['id', 'trade']
        depth = 3
