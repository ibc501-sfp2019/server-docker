from django.urls import path
from . import controllers

urlpatterns = [
    path('locations/', controllers.get_balls_location_list, name='locations'),
]
