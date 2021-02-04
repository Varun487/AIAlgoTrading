from django.db import models

# Create your models here.
class ExampleDataFeederModel(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
