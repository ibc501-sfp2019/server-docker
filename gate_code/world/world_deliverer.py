from django.http import JsonResponse
from deliverer import Deliverer
from common.enum import HttpMethods

class WorldDeliverer(Deliverer):
    @staticmethod
    def start_game(request):
        to = 'world:8000/core/start'
        method = HttpMethods.GET
        params = {
            'play_id' : request.GET.get('play_id', '')
        }
        return WorldDeliverer.send(request, to, method, params)

    @staticmethod
    def end_game(request):
        to = 'world:8000/core/end'
        method = HttpMethods.GET
        params = {
            'play_id' : request.GET.get('play_id', '')
        }
        return WorldDeliverer.send(request, to, method, params)
