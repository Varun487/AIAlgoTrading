from rest_framework import serializers
from .models import ExampleDataFeederModel, Company, Indicators, ImmutableData, CalculatedCandleStick


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

class CandleStickSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculatedCandleStick
        fields = ['open', 'low', 'high', 'close', 'volume', 'company', 'time_stamp', 'time_period']
        depth = 1
