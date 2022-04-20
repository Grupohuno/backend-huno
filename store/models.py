from operator import mod
from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=180)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
