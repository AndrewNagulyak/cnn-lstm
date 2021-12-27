from django.db import models


class StockSet(models.Model):
    nameOfSet = models.CharField(max_length=200)