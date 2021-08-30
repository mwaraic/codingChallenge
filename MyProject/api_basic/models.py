from datetime import datetime
from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, PositiveIntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Vehicle(models.Model):
    unit=CharField(primary_key=True, max_length=100)
    mileage=PositiveIntegerField()
    manufacturer=CharField(max_length=100)
    status=CharField(max_length=100)

class Day_Mileage(models.Model):
    unit=ForeignKey(Vehicle, models.DO_NOTHING, db_column='unit')
    mileage=PositiveIntegerField()
    date=DateField()
    
    class Meta:
        
        unique_together=(('unit', 'date'))


    