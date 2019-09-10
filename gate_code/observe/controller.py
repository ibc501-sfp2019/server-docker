from django.http import JsonResponse
from time import time
from random import random
from os import environ
import requests
from deliverer import Deliverer

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
