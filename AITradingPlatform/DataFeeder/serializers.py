from rest_framework import serializers
from .models import ExampleDataFeederModel, Company

class ExampleDataFeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleDataFeederModel
        fields = ['name']

class ListCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'ticker', 'sector']


