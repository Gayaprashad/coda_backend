from django.db import models

# Create your models here.

class Cars (models.Model):
    reg_no = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    from_date = models.DateField(blank=True,null=True)
    to_date =models.DateField(blank=True, null=True)
    userId = models.IntegerField(blank=True,null=True) 
    booked = models.BooleanField()
    def __str__(self):
        return self.reg_no