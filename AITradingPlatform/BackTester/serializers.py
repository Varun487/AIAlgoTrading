from rest_framework import serializers
from .models import ExampleBackTesterModel

class ExampleBackTesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleBackTesterModel
        fields = ['name']
