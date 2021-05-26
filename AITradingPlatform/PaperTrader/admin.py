from django.contrib import admin
from .models import ExamplePaperTraderModel, PaperTradeOrder, PaperTradedStrategies

# Register your models here.
admin.site.register(ExamplePaperTraderModel)
admin.site.register(PaperTradeOrder)
admin.site.register(PaperTradedStrategies)
