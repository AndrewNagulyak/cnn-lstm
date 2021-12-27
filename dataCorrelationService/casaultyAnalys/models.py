from django.db import models


class CasaultySet(models.Model):
    nameOfSet = models.CharField(max_length=200)