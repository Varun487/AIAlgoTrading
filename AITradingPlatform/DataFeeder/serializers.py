from rest_framework import serializers
from .models import ExampleDataFeederModel, Company, TimeStamp

class ExampleDataFeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleDataFeederModel
        fields = ['name']

class ListCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'ticker', 'sector']

class TimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStamp
        fields = ['date_time']
