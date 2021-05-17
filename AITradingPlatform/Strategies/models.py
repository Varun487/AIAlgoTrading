from django.db import models

# Create your models here.
class ExampleStrategiesModel(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200, blank=False)
    ticker = models.CharField(max_length=100, blank=False)
    sector = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.name

class Strategy(models.Model):
    name = models.CharField(max_length=200, blank=False)
    desc = models.CharField(max_length=500, blank=False)
    sector = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return f"Strategy: {self.name}, Description: {self.desc}"

class Orders(models.Model):
    ORD_TYPE = ['Buy','Sell'] #[('B','Buy'),('S','Sell')]
    ORD_CAT = ['Market','Limit'] #[('M','Market'),('L','Limit')]
    ORD_OWN = ['Back Tester','Paper Trader'] #[('BT','Back Tester'),('PT','Paper Trader')]
    PROFIT_LOSS = ['Profit','Loss'] #[('P','Profit'),('L','Loss')]
    order_type = models.CharField(max_length=4, choices=ORD_TYPE, default='Default')
    order_category = models.CharField(max_length=6, choices=ORD_CAT, default='Default')
    order_owner = models.CharField(max_length=15, choices=ORD_OWN, default='Default')
    strategy = models.ForeignKey(to=Strategy, on_delete=models.CASCADE)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()
    profit = models.IntegerField(blank=True)
    stop_loss = models.IntegerField()
    profit_loss = models.CharField(max_length=6,choices=PROFIT_LOSS,blank=True)

    def __str__(self):
        return f"Order Type: {self.order_type}, Order Owner: {self.order_owner}, Profit: {self.profit}, Strategy: {self.strategy.name}"

