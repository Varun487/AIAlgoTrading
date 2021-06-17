from django.contrib import admin
from .models import ExampleBackTesterModel, BackTestReport, BackTestTrade

# Register your models here.
admin.site.register(ExampleBackTesterModel)
admin.site.register(BackTestReport)
admin.site.register(BackTestTrade)
