from rest_framework import serializers
from .models import ExampleStrategiesModel, StrategyType


class ExampleStrategiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleStrategiesModel
        fields = ['name']


class AllStrategiesStrategyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyType
        fields = ['id', 'name', 'description']


class StrategyDataStrategyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategyType
        fields = ['id', 'name', 'description', 'stock_selection', 'entry_criteria', 'exit_criteria', 'stop_loss_method',
                  'take_profit_method']
