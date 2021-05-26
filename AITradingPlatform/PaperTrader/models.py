from django.db import models
from DataFeeder.models import Company
from Strategies.models import Orders, Strategy


# Create your models here.
class ExamplePaperTraderModel(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class PaperTradedStrategies(models.Model):
    strategy = models.ForeignKey(to=Strategy, on_delete=models.CASCADE)
    column = models.CharField(max_length=100)
    time_period = models.IntegerField()
    sigma = models.IntegerField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, default=0)
    name = models.CharField(default=f"None", max_length=200)

    def __str__(self):
        return f"Strategy: {self.strategy}, Company: {self.company} Column: {self.column}, Time_period: {self.time_period}, Sigma: {self.sigma}"


class PaperTradeOrder(models.Model):
    order = models.ForeignKey(to=Orders, on_delete=models.CASCADE)
    strategy = models.ForeignKey(to=PaperTradedStrategies, on_delete=models.CASCADE)
    live_order = models.BooleanField(default=False)
    price_bought = models.FloatField(default=0.0)
    percentage_change = models.FloatField(default=0.0)

    def __str__(self):
        return f"Order: {self.order}, Strategy: {self.strategy}, Live_order: {self.live_order}"
