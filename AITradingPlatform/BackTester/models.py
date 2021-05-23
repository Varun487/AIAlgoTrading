from django.db import models

# Create your models here.
class ExampleBackTesterModel(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Backtest(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    risk = models.FloatField()
    profit_loss = models.FloatField()
    initial_account_size = models.FloatField()
    final_account_size = models.FloatField()

    def __str__(self):
        return self.final_account_size
