from django.urls import path 
from .views import VehicleCreateView,VehicleListView,VehicleDetailView 

urlpatterns = [
    path('',VehicleListView.as_view()),
    path('create/',VehicleCreateView.as_view()),
    path('<pk>',VehicleDetailView.as_view()),
    
    
]