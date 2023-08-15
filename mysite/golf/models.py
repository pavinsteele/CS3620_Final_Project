from django.db import models


# Create your models here.

class Profile(models.Model):
    course = models.CharField(max_length=200)
    score = models.IntegerField()
    fairways = models.IntegerField()
    putts = models.IntegerField()
    greens = models.IntegerField()
    pars = models.IntegerField()
    birdies = models.IntegerField()
    summary = models.TextField(max_length=2000)
