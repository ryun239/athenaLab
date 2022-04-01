from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    studend_id = models.CharField(max_length=10)