from rest_framework import serializers
from .models import ExampleStrategiesModel, Strategy , Orders

class ExampleStrategiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleStrategiesModel
        fields = ['name']

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ['name','desc', 'sector']
        depth = 1

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['ORD_TYPE', 'ORD_CAT', 'ORD_OWN', 'PROFIT_LOSS', ' order_type', ' order_category', ' order_owner'
                 ,'strategy', 'company', 'time_stamp', 'profit', 'stop_loss', 'profit_loss']
        depth = 1
