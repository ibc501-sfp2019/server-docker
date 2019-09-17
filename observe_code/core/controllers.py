from django.http import JsonResponse
from django.db import IntegrityError
from django.utils import timezone
from common.enum import HttpResponses
from .models import Plays, PlayStatus, Balls, Locations

def get_balls_location_list(request):
    status = HttpResponses.OK.value
    data = []
    try:
        play = Plays.objects.filter(id=request.GET.get('play_id')).filter(status=PlayStatus.IN_PROGRESS.value).first()
        print(play)
        now = timezone.now()
        for ball in Balls.objects.filter(play=play):
            print(ball)
            locations = []
            for l in Locations.objects.filter(ball=ball).filter(time__gte=now).order_by('time')[:120]:
                locations.append(l.to_json())
            
            data.append({
                'ball_id'   : ball.id,
                'data'      : locations
            })
    except Plays.DoesNotExist:
        status = HttpResponses.FORBIDDEN.value
    except IntegrityError:
        status = HttpResponses.INTERNER_SERVER_ERROR.value
    return JsonResponse({
        'status' : status,
        'data'   : data
    })
