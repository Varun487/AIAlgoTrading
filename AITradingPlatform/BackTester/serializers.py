from rest_framework import serializers
from .models import ExampleBackTesterModel , BackTestOrder

class ExampleBackTesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleBackTesterModel
        fields = ['name']

class BackTestOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackTestOrder
        fields = [' order', 'backtestreport', 'account_size']
        depth = 1


