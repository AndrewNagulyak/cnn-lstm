from django.db import models


class CorrelationSet(models.Model):
    nameOfSet = models.CharField(max_length=200)