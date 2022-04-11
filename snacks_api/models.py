from django.db import models

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    description = models.CharField(max_length=300)
