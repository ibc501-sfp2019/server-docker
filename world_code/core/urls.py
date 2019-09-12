from django.urls import path
from . import controllers

urlpatterns = [
    path('end/', controllers.end_game, name='end_game'),
    path('start/', controllers.start_game, name='start_game'),
]
