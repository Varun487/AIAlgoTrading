from django.contrib import admin
from .models import ExamplePaperTraderModel, PaperTradedStrategy, CurrentQuote, PaperTrade, PaperSignal

# Register your models here.
admin.site.register(ExamplePaperTraderModel)
admin.site.register(PaperTradedStrategy)
admin.site.register(CurrentQuote)
admin.site.register(PaperSignal)
admin.site.register(PaperTrade)
