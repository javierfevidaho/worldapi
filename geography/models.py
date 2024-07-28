# models.py
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, default='TEMP')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
