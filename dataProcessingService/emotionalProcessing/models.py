from django.db import models


class EmotionalSet(models.Model):
    nameOfSet = models.CharField(max_length=200)