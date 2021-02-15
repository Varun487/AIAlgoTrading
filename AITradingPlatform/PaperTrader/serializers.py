from rest_framework import serializers
from .models import ExamplePaperTraderModel

class ExamplePaperTraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamplePaperTraderModel
        fields = ['name']
