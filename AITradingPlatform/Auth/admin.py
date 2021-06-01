from django.contrib import admin
from .models import Login, ExampleAuthModel

# Register your models here.
admin.site.register(Login)
admin.site.register(ExampleAuthModel)