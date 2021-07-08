from django.db import models
from strategies.models import StrategyConfig, Company, TickerData, Trade, Signal


# Example model of no consequence
class ExamplePaperTraderModel(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class PaperTradedStrategy(models.Model):
    strategy_config = models.ForeignKey(
        to=StrategyConfig,
        on_delete=models.CASCADE,
        blank=False, null=False
    )
    company = models.ForeignKey(
        to=Company,
        on_delete=models.CASCADE,
        blank=False, null=False
    )
    live = models.BooleanField()

    def __str__(self):
        return f"{self.strategy_config} {self.company} {self.live}"


class CurrentQuote(models.Model):
    company = models.ForeignKey(
        to=Company,
        on_delete=models.CASCADE,
        blank=False, null=False
    )
    ticker_data = models.ForeignKey(
        to=TickerData,
        on_delete=models.CASCADE,
        blank=False, null=False
    )
    last_updated = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.company} {self.ticker_data} {self.last_updated}"


class PaperTrade(models.Model):
    trade = models.ForeignKey(
        to=Trade,
        on_delete=models.CASCADE,
        blank=False, null=False
    )
    paper_traded_strategy = models.ForeignKey(
        to=PaperTradedStrategy,
        on_delete=models.CASCADE,
        blank=False, null=False
    )
    live = models.BooleanField()
    take_profit = models.FloatField(default=0.0)
    stop_loss = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.paper_traded_strategy} {self.trade} {self.live}"


class PaperSignal(models.Model):
    signal = models.ForeignKey(
        to=Signal,
        on_delete=models.CASCADE,
        blank=False, null=False
    )
    paper_traded_strategy = models.ForeignKey(
        to=PaperTradedStrategy,
        on_delete=models.CASCADE,
        blank=False, null=False
    )
    executed = models.BooleanField()
    take_profit = models.FloatField(default=0.0)
    stop_loss = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.paper_traded_strategy} {self.signal} {self.executed}"
