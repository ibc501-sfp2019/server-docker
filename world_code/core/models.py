from django.db import models
from django.utils import timezone
from enum import Enum
from datetime import timedelta
import numpy as np

class PlayStatus(Enum):
    PREPARING = 0
    IN_PROGRESS = 1
    GATE_SET = 2

class Plays(models.Model):
    status = models.SmallIntegerField()
    name = models.CharField(max_length=256)
    started_at = models.DateTimeField(null=True)
    ended_at = models.DateTimeField(null=True)

class Balls(models.Model):
    play = models.ForeignKey(Plays, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def move(self, term=200, interval=0.05):
        currunt_location = Locations.objects.filter(ball=self).order_by(models.F('time').desc()).first()
        if currunt_location is None:
            currunt_location = Locations(ball=self, x=0.0, y=0.0, z=0.0, time=timezone.now())
            currunt_location.save()
        p = np.array(
            [currunt_location.x, currunt_location.y, currunt_location.z]
        )
        v = np.random.uniform(low=-0.5, high=0.5, size=(3,))
        time = currunt_location.time
        uper_limit = np.array([1, 1, 1])
        lower_limit = np.array([-1, 0, -1])
        for i in range(term):
            p += v*interval
            p[p > uper_limit] = uper_limit[p > uper_limit]
            p[lower_limit > p] = lower_limit[lower_limit > p]
            time += timedelta(seconds=interval)
            l = Locations(ball=self, x=p[0], y=p[1], z=p[2], time=time)
            l.save()

class Locations(models.Model):
    ball = models.ForeignKey(Balls, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    time = models.DateTimeField()
