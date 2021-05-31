from django.db import models


# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"Username: {self.username}, Period: {str(self.password)}"
