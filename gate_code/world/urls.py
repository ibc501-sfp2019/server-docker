from django.urls import path
from .world_deliverer import WorldDeliverer

urlpatterns = [
    path('end/', WorldDeliverer.end_game, name='end_game'),
    path('start/', WorldDeliverer.start_game, name='start_game'),
]
