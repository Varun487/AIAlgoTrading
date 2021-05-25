from django.db import models
from Strategies.models import Orders, Strategy

# Create your models here.
class ExamplePaperTraderModel(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class PaperTradeOrder(models.Model):
    order = models.ForeignKey(to=Orders, on_delete=models.CASCADE)
    strategy = models.ForeignKey(to=Strategy, on_delete=models.CASCADE)
    live_order = [('L', 'Live'), ('H', 'Historical')]
    percentage_change = models.FloatField()

    def __str__(self):
        return f"Order: {self.order}, Strategy: {self.strategy}, Live_order: {self.live_order}"



