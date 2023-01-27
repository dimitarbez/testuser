from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, null=False)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='uploaded_images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sold_date = models.DateField(default=now())


class SoldProduct(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, null=True, on_delete=models.CASCADE)
