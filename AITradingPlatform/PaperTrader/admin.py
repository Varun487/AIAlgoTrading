from django.contrib import admin
from .models import ExamplePaperTraderModel, PaperTradeOrder

# Register your models here.
admin.site.register(ExamplePaperTraderModel)
admin.site.register(PaperTradeOrder)
