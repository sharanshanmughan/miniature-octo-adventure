from django.contrib import admin

from .models import Vehicle

@admin.register(Vehicle)

class VehicleAdmin(admin.ModelAdmin):
    list_display=('car_number','mobile_number','entry')