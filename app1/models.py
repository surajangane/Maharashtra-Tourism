from django.db import models


class Booking(models.Model):
    name=models.CharField(max_length=50)
    where=models.CharField(max_length=50)
    guest=models.IntegerField()
    arrivals=models.DateField()
    leaving=models.DateField()
    
    
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    number=models.IntegerField()
    subject=models.CharField(max_length=100)
    message=models.TextField()