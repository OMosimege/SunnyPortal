from django.db import models


class Energy(models.Model):
    kilowatts = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
