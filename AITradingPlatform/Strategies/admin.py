from django.contrib import admin
from .models import ExampleStrategiesModel,Company, Strategy, Orders

# Register your models here.
admin.site.register(ExampleStrategiesModel)
admin.site.register(Company)
admin.site.register(Strategy)
admin.site.register(Order)
