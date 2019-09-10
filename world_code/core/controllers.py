from django.http import JsonResponse
from django.db import IntegrityError
from django.utils import timezone
from common.enum import HttpResponses
from .models import Plays, PlayStatus

def start_game(request):
    status = HttpResponses.OK.value
    try:
        play = Plays.objects.get(id=request.GET.get('play_id'))
        play.status = PlayStatus.IN_PROGRESS.value
        play.started_at = timezone.now()
        play.ended_at = None
        play.save()
    except Plays.DoesNotExist:
        status = HttpResponses.FORBIDDEN.value
    except IntegrityError:
        status = HttpResponses.INTERNER_SERVER_ERROR.value
    return JsonResponse({'status':status})

def end_game(request):
    status = HttpResponses.OK.value
    try:
        play = Plays.objects.get(id=request.GET.get('play_id'))
        play.status = PlayStatus.GATE_SET.value
        play.ended_at = timezone.now()
        play.save()
    except Plays.DoesNotExist:
        status = HttpResponses.FORBIDDEN.value
    except IntegrityError:
        status = HttpResponses.INTERNER_SERVER_ERROR.value
    return JsonResponse({'status':status})
