from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from core.models import Plays, Balls, Locations, PlayStatus

@transaction.atomic
class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            play_list = Plays.objects.filter(status=PlayStatus.IN_PROGRESS.value)
            for play in play_list:
                with transaction.atomic():
                    for b in Balls.objects.filter(play=play):
                        b.move()
            self.stdout.write("Snitch Acitevate Success")
        except Exception as e:
            self.stderr.write("Snitch Activate Fail with e : " + str(e))
