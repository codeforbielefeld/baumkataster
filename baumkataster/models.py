from django.db import models

# Create your models here.
class User(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Tree(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    height = models.IntegerField(default=0)
    diameter = models.IntegerField(default=0)
    kind = models.CharField(max_length=100)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    type_of_care = models.IntegerField(default=0)
    user_list = models.ManyToManyField(User)

    def update(self, data):
        for attribute in ["name", "height", "diameter", "kind", "long", "lat", "type_of_care"]:
            setattr(self, attribute, data[attribute])
