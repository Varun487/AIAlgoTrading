from rest_framework import serializers
from .models import ExampleStrategiesModel, Strategy

class ExampleStrategiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleStrategiesModel
        fields = ['name']

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ['name','desc', 'sector']
        depth = 1