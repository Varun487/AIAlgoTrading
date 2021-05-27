from rest_framework import serializers
from .models import ExamplePaperTraderModel,  PaperTradedStrategies


class ExamplePaperTraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamplePaperTraderModel
        fields = ['name']


class PaperTradedStrategiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperTradedStrategies
        fields = ['strategy', 'company','column','time_period','sigma','name']
        depth =1

