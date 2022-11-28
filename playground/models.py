from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField();
    prices = models.DecimalField(max_digits=6, decimal_places=2)
