from rest_framework import serializers
from .models import ExamplePaperTraderModel,  PaperTradedStrategies, PaperTradeOrder


class ExamplePaperTraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamplePaperTraderModel
        fields = ['name']


class PaperTradedStrategiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperTradedStrategies
        fields = ['order', 'strategy', 'live_order']

class PaperTradeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperTradeOrder
        fields = ['order', 'strategy', 'live_order', 'price_bought', 'percentage_change']
        depth = 1


