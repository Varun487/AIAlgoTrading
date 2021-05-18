from rest_framework import serializers
from .models import ExampleDataFeederModel, Company, Indicators, ImmutableData


class ExampleDataFeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleDataFeederModel
        fields = ['name']


class ListCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'ticker', 'sector']


class IndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicators
        fields = ['value', 'name', 'column', 'indicator_time_period', 'candle_stick']
        depth = 1
