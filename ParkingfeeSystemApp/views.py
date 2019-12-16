from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Vehicle
from .serializers import vehicleSerializer

class VehicleListView(ListAPIView):
        queryset = Vehicle.objects.all()
        serializer_class = vehicleSerializer
        filter_backends = (SearchFilter, OrderingFilter)
        search_fields = ('car_number',"mobile_number")
class VehicleDetailView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = vehicleSerializer
    
class VehicleCreateView(CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = vehicleSerializer