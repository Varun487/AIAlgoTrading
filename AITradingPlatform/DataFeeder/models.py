from django.db import models


class ExampleDataFeederModel(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200, blank=False)
    ticker = models.CharField(max_length=100, blank=False)
    sector = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.name

class ImmutableData(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()
    time_period = models.CharField(default='daily', max_length=5)

    def __str__(self):
        return f"Company: {self.company.name}, Period: {str(self.time_period)}, Time: {str(self.time_stamp)} "


class CalculatedCandleStick(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()

    def __str__(self):
        return self.company.name


class Indicators(models.Model):
    sma = models.FloatField()
    stddev = models.FloatField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()

    def __str__(self):
        return self.company.name
