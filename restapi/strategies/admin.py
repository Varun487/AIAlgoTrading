from django.contrib import admin
from .models import ExampleStrategiesModel, Company, TickerData, IndicatorType, StrategyType, StrategyConfig, Signal,\
    Order, Trade, VisualizationType

# Register your models here.
admin.site.register(ExampleStrategiesModel)
admin.site.register(Company)
admin.site.register(TickerData)
admin.site.register(IndicatorType)
admin.site.register(StrategyType)
admin.site.register(StrategyConfig)
admin.site.register(Signal)
admin.site.register(Order)
admin.site.register(Trade)
admin.site.register(VisualizationType)
