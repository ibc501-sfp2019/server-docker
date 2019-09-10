from deliverer import Deliverer
from common.enum import HttpMethods

class ObserveDeliverer(Deliverer):
    @staticmethod
    def get_ball_location_list(request):
        to = 'observe:8000/core/locations'
        method = HttpMethods.GET
        params = {
            'play_id' : request.GET.get('play_id', '')
        }
        return ObserveDeliverer.send(request, to, method, params)
