# from operator import mod
from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=180)
    web_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=180)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True,
                                 null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=180)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE,
                                 blank=True, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    blank=True, null=True)
    sku = models.CharField(max_length=180)
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    size = models.DecimalField()
    size_metric = models.CharField(max_length=180)

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.IntegerField()
    date = models.DateField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,
                                   blank=True, null=True)

    def __str__(self):
        return self.price


class Local(models.Model):
    name = models.CharField(max_length=180)
    address = models.CharField(max_length=180)
    province = models.CharField(max_length=180)
    city = models.CharField(max_length=180)
    longitude = models.FloatField()
    latitude = models.FloatField()
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE,
                                 blank=True, null=True)

    def __str__(self):
        return self.name
