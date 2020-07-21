from django.db import models

# Create your models here.

class dashboardData(models.Model):
    onroad= models.IntegerField()
    available =models.IntegerField()
    mostInDemandLoc = models.CharField(max_length=40)
    mostInDemandMod = models.CharField(max_length=40)