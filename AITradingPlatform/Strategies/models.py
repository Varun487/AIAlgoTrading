from datetime import datetime

from django.db import models
from DataFeeder.models import Company, ImmutableData


# Create your models here.
from django.utils.timezone import make_aware


class ExampleStrategiesModel(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Strategy(models.Model):
    name = models.CharField(max_length=200, blank=False)
    desc = models.TextField()
    sector = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return f"Strategy: {self.name}"


class Orders(models.Model):
    ORD_TYPE = [('B', 'Buy'), ('S', 'Sell'), ('G', 'Get out of all positions')]  # ['Buy','Sell']
    ORD_CAT = [('M', 'Market'), ('L', 'Limit')]  # ['Market','Limit']
    ORD_OWN = [('BT', 'Back Tester'), ('PT', 'Paper Trader')]  # ['Back Tester','Paper Trader']
    PROFIT_LOSS = [('P', 'Profit'), ('L', 'Loss')]  # ['Profit','Loss']
    order_type = models.CharField(max_length=4, choices=ORD_TYPE, default='Default')
    order_category = models.CharField(max_length=6, choices=ORD_CAT, default='Default')
    order_owner = models.CharField(max_length=15, choices=ORD_OWN, default='Default')
    strategy = models.ForeignKey(to=Strategy, on_delete=models.CASCADE)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, default=0)
    time_stamp = models.DateTimeField(default=make_aware(datetime.strptime('2021-05-1 00:00:00', '%Y-%m-%d %H:%M:%S')))
    profit = models.IntegerField(blank=True)
    stop_loss = models.IntegerField(blank=True)
    profit_loss = models.CharField(max_length=6, choices=PROFIT_LOSS, blank=True)

    def __str__(self):
        return f"Order Type: {self.order_type}, Order Owner: {self.order_owner}, Profit: {self.profit}, Strategy: {self.strategy.name}"
