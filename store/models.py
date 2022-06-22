from django.db import models


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=180)
    web_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=180)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=180)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True, null=True, related_name="store")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    sku = models.CharField(max_length=180)
    brand = models.CharField(max_length=180)
    size = models.CharField(max_length=180, null=True)
    image_url = models.CharField(max_length=280)
    page_url = models.CharField(max_length=280)
    is_promotion = models.BooleanField(default=False)

    def price(self):
        last_price = Price.objects.filter(product_id=self).last()

        if last_price is None:
            return
        return last_price.price

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.IntegerField()
    date = models.DateField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name="product")

    def __str__(self):
        return str(self.price)
