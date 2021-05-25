from django.contrib import admin
from .models import ExampleBackTesterModel, BackTestReport, BackTestOrder

# Register your models here.
admin.site.register(ExampleBackTesterModel)
admin.site.register(BackTestReport)
admin.site.register(BackTestOrder)