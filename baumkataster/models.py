from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Tree(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField(default=0)
    diameter = models.IntegerField(default=0)
    kind = models.CharField(max_length=100)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    type_of_care = models.IntegerField(default=0)