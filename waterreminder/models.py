from django.db import models

from flower.models import Flower

# Create your models here.

class Reminder(models.Model):
    daily = 'D'
    weekly = 'W'
    REMINDER = (
        (daily , ' daily '),
        (weekly , ' weekly ')
    )
    how_often = models.CharField(max_length=200,
        choices = REMINDER)
    pub_date = models.DateTimeField('date published')

    flower = ForeignKey(Flower, on_delete=models.CASCADE)
