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

class TimeStamp(models.Model):
    date_time = models.DateTimeField()

    def __str__(self):
        return str(self.date_time)
        #return str(self.date_time.strftime("%Y%m%d-%H:%M:%S")
        #return self.date_time   ---error

class ImmutableData(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    timestamp = models.ForeignKey(to=TimeStamp, on_delete=models.CASCADE)

    def __str__(self):
        return self.timestamp + "_" + self.company

class CalculatedCandleStick(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    timestamp = models.ForeignKey(to=TimeStamp, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.timestamp + "_" + self.company

class Indicators(models.Model):
    sma = models.FloatField()
    stddev = models.FloatField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    timestamp = models.ForeignKey(to=TimeStamp, on_delete=models.CASCADE)

    def __str__(self):
        return self.timestamp + "_" + self.company
