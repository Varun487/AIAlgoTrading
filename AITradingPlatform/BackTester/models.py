from django.db import models

# Create your models here.
class ExampleBackTesterModel(models.Model):
    name = models.CharField(max_length=50, blank=False)
    new = models.CharField(max_length=1, default='a')

    def __str__(self):
        return self.name
