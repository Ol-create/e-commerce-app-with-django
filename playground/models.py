from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField();
    prices = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
