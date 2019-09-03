from django.urls import path
from . import controller

urlpatterns = [
    path('', controller.get_position_list, name='get_position_list'),
    path('end/', controller.end_game, name='end_game'),
    path('start/', controller.start_game, name='start_game'),
]
