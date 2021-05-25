from django.db import models
from Strategies.models import Orders, Strategy
from DataFeeder.models import Company

# Create your models here.
class ExampleBackTesterModel(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class BackTestReport(models.Model):
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    risk_ratio = [('S', 'Stoploss'), ('T', 'Takeprofit')]
    max_risk = models.FloatField()
    initial_account_size = models.FloatField()
    final_account_size = models.FloatField()
    total_profit_loss = models.FloatField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    strategy = models.ForeignKey(to=Strategy,on_delete=models.CASCADE)

    def __str__(self):
        return f"Company: {self.company},Start_date_time : {self.start_date_time },End_date_time : {self.end_date_time}," \
               f"Strategy : {self.strategy}"

class BackTestOrder(models.Model):
    order = models.ForeignKey(to=Orders, on_delete=models.CASCADE)
    backtestreport = models.ForeignKey(to=BackTestReport, on_delete=models.CASCADE)
    account_size = models.FloatField()

    def __str__(self):
        return f"Order: {self.order }, Backtestreport: {self.backtestreport}"
