from django.urls import path
from . import controller

urlpatterns = [
    path('', controller.get_position_list, name='get_position_list'),
]
