from django.db import models

from strategies.models import StrategyType, StrategyConfig, Trade

# specify TickData time_period choices
BACK_TEST_REPORT_STATUS_CHOICES = (
    ("1", "Pending"),
    ("2", "Running"),
    ("3", "Completed"),
)


# Example model of no consequence
class ExampleBackTesterModel(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


# BackTest report
class BackTestReport(models.Model):
    status = models.CharField(
        max_length=100,
        choices=BACK_TEST_REPORT_STATUS_CHOICES,
        default="1",
    )
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    strategy_type = models.ForeignKey(to=StrategyType, on_delete=models.CASCADE)
    strategy_config = models.ForeignKey(to=StrategyConfig, on_delete=models.CASCADE)
    total_returns = models.FloatField()
    total_trades = models.IntegerField()
    profit_trades = models.IntegerField()
    profit_trades_percent = models.FloatField()

    def __str__(self):
        return f"{self.status}"


# BackTest Trade - Linking each trade to a BackTest Report
class BackTestTrade(models.Model):
    trade = models.ForeignKey(to=Trade, on_delete=models.CASCADE)
    back_test_report = models.ForeignKey(to=BackTestReport, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trade} {self.back_test_report}"
