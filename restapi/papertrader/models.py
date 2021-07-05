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
