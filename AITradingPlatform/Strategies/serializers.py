from rest_framework import serializers
from .models import ExampleStrategiesModel

class ExampleStrategiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleStrategiesModel
        fields = ['name']
