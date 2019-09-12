from django.db import models
from enum import Enum
from datetime import timedelta

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

class Locations(models.Model):
    ball = models.ForeignKey(Balls, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    time = models.DateTimeField()

    def to_json(self):
        return {
            'timestamp' : self.time.timestamp(),
            'location' : {
                'x' : self.x,
                'y' : self.y,
                'z' : self.z
            }
        }
