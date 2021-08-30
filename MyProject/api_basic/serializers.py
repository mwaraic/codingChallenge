from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vehicle
        fields= ['mileage']

class VehicleGetSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vehicle
        fields= '__all__'

  

