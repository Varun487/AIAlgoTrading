from django.contrib import admin
from .models import ExampleDataFeederModel, Company, TimeStamp, ImmutableData, CalculatedCandleStick, Indicators

# Register your models here.
admin.site.register(ExampleDataFeederModel)
admin.site.register(Company)
admin.site.register(TimeStamp)
admin.site.register(ImmutableData)
admin.site.register(CalculatedCandleStick)
admin.site.register(Indicators)