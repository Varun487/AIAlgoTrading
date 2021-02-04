from rest_framework import serializers
from .models import ExampleDataFeederModel

class ExampleDataFeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleDataFeederModel
        fields = ['name']
