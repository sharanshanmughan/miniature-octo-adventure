from django.db import models

class Vehicle(models.Model):
    car_number = models.CharField(max_length=50,blank=True,null=True)
    mobile_number = models.IntegerField(max_length=10,blank=True,null=True)
    entry = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.car_number
