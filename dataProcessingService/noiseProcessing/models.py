from django.db import models


class TwitterProcessingSet(models.Model):
    nameOfSet = models.CharField(max_length=200)