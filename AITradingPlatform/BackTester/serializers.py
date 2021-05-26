from rest_framework import serializers
from .models import ExampleBackTesterModel, BackTestOrder, BackTestReport


class ExampleBackTesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleBackTesterModel
        fields = ['name']

class BackTestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackTestReport
        fields = ['start_date_time', 'end_date_time', 'max_risk', 'risk_ratio', 'initial_account_size', 'final_account_size', 'total_profit_loss', 'company', 'strategy']

class BackTestOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackTestOrder
        fields = [' order', 'backtestreport', 'account_size']
        depth = 1


class BackTestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackTestReport
        fields = [' start_date_time', 'end_date_time', 'max_risk', 'risk_ratio', 'initial_account_size ', 'final_account_size',
                  'total_profit_loss', 'company', 'strategy']
        depth = 1


