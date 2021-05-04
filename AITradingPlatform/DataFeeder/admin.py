from django.contrib import admin
from .models import ExampleDataFeederModel, Company, TimeStamp, ImmutableData

# Register your models here.
admin.site.register(ExampleDataFeederModel)
admin.site.register(Company)
admin.site.register(TimeStamp)
admin.site.register(ImmutableData)
