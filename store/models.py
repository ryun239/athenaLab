from operator import mod
from platform import java_ver
from pyexpat import model
from django.db import models
from django.forms import IntegerField


# Create your models here.
class Stock(models.Model):
    Idx = models.IntegerField()
    meterial = models.CharField(max_length=32)
    quntity = models.IntegerField()


# class Inventory(models.Model):
#     Idx = IntegerField()


class Bread(models.Model):
    Idx = models.IntegerField()
    Bread_Kind = models.CharField(max_length=12)
    BreadAmount = models.IntegerField()

class Toping(models.Model):
    Idx = models.IntegerField()
    TopingKind = models.CharField(max_length=12)
    TopingAmount = models.IntegerField()

class Ham(models.Model):
    Idx = models.IntegerField()
    HamingKind = models.CharField(max_length=12)
    HamingAmount = models.IntegerField()