from django.db import models

from strategies.models import StrategyType, StrategyConfig, Trade, Company

# specify TickData time_period choices
BACK_TEST_REPORT_STATUS_CHOICES = (
    ("1", "Pending"),
    ("2", "Running"),
    ("3", "Completed"),
)


# Example model of no consequence
class ExampleBackTesterModel(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


# BackTest report
class BackTestReport(models.Model):
    status = models.CharField(
        max_length=100,
        choices=BACK_TEST_REPORT_STATUS_CHOICES,
        default="1",
        blank=False,
        null=False,
    )
    start_date_time = models.DateTimeField(blank=False, null=False)
    end_date_time = models.DateTimeField(blank=False, null=False)
    strategy_type = models.ForeignKey(to=StrategyType, on_delete=models.CASCADE, blank=False, null=False)
    strategy_config = models.ForeignKey(to=StrategyConfig, on_delete=models.CASCADE, blank=False, null=False)
    total_returns = models.FloatField(blank=False, null=False)
    total_returns_percent = models.FloatField(blank=False, null=False, default=0.0)
    total_trades = models.IntegerField(blank=False, null=False)
    profit_trades = models.IntegerField(blank=False, null=False)
    profit_trades_percent = models.FloatField(blank=False, null=False)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.company} {self.start_date_time} {self.end_date_time} {self.total_returns}"


# BackTest Trade - Linking each trade to a BackTest Report
class BackTestTrade(models.Model):
    trade = models.ForeignKey(to=Trade, on_delete=models.CASCADE, blank=False, null=False)
    back_test_report = models.ForeignKey(to=BackTestReport, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.trade} {self.back_test_report}"
