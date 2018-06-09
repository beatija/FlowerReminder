from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=200)
