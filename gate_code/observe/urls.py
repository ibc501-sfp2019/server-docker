from django.urls import path
from .observe_deliverer import ObserveDeliverer

urlpatterns = [
    path('', ObserveDeliverer.get_ball_location_list, name='get_position_list'),
]
