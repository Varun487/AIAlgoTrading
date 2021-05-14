from django.contrib import admin
from .models import ExampleDataFeederModel, Company, ImmutableData, CalculatedCandleStick, Indicators

# Register your models here.
admin.site.register(ExampleDataFeederModel)
admin.site.register(Company)
admin.site.register(ImmutableData)
admin.site.register(CalculatedCandleStick)
admin.site.register(Indicators)