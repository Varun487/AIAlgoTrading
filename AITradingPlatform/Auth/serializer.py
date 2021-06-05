from rest_framework import fields, serializers
from .models import ExampleAuthModel, Login




class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['username', 'password']
