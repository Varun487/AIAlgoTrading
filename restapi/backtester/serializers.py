from rest_framework import serializers
from .models import ExampleBackTesterModel, BackTestTrade, BackTestReport


class ExampleBackTesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleBackTesterModel
        fields = ['name']


class BackTestTradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackTestTrade
        fields = ['trade', ' back_test_report']


class BackTestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackTestReport
        fields = ['status', 'start_date_time', 'end_date_time', 'strategy_type', 'strategy_config', 'total_returns',
                  'total_returns_percent',
                  'total_trades', 'profit_trades', 'profit_trades_percent', 'company']
