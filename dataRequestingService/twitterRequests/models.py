from django.db import models


class TwitterSet(models.Model):
    nameOfSet = models.CharField(max_length=200)