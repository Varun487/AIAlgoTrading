from rest_framework import serializers
from .models import ExamplePaperTraderModel,  PaperTradedStrategies


class ExamplePaperTraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamplePaperTraderModel
        fields = ['name']


class PaperTradedStrategiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperTradedStrategies
        fields = ['order', 'strategy', 'live_order']

