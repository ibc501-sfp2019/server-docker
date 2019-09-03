from django.http import JsonResponse
from time import time
from random import random
from os import environ

def start_game(request):
    environ['PLAY_FLG'] = '1'
    return JsonResponse({'status':200})

def get_position_list(requset):
    data = []
    if environ['PLAY_FLG'] == '1':
        # On play
        now = time()
        for i in range(50):
            data.append({
                'timestamp' : int((now + 0.1 * i) * 1000),
                'location' : {
                    'x' : random() * 20,
                    'y' : random() * 20,
                    'z' : random() * 20
                }
            })
    res = {
        'status': 200,
        'data' : data
    }
    
    return JsonResponse(res)

def end_game(requset):
    environ['PLAY_FLG'] = '0'
    return JsonResponse({'status':200})
