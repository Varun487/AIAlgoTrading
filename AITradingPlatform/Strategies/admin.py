from django.contrib import admin
from .models import ExampleStrategiesModel, Strategy, Orders

# Register your models here.
admin.site.register(ExampleStrategiesModel)
admin.site.register(Strategy)
admin.site.register(Orders)
