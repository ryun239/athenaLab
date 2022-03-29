from pyexpat import model
from django.db import models


# Create your models here.
class Stock(models.Model):
    Idx = models.IntegerField()
    meterial = models.CharField(max_length=32)
    quntity = models.IntegerField()