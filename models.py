# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    app_label = 'myfirstproject'

class Item(models.Model):
    sku = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255)
    stock_status = models.CharField(max_length=20)
    available_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    

