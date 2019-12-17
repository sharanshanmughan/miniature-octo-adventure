from rest_framework import serializers
from .models import Vehicle

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields=('car_number','mobile_number')