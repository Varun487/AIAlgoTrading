from django.contrib import admin
from .models import ExampleBackTesterModel, Backtest

# Register your models here.
admin.site.register(ExampleBackTesterModel)
admin.site.register(Backtest)