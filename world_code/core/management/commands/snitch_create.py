from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from core.models import Plays, Balls, Locations, PlayStatus

class Command(BaseCommand):
    help = 'Create Snitch'

    def add_arguments(self, parser):
        parser.add_argument('play_name', nargs='?', type=str)
        parser.add_argument('num_snitch', nargs='?', type=int, default=1)

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            play_name = options['play_name']
            with transaction.atomic():
                play = Plays(name=play_name,status=PlayStatus.PREPARING.value)
                play.save()
                num_snitch = options['num_snitch']
                ball_list = []
                for i in range(num_snitch):
                    snitch_name = play_name + '_' + str(i)
                    ball = Balls(play=play, name=snitch_name)
                    ball.save()
                    ball_list.append(ball)
            self.stdout.write("Snitch Create Success")
        except Exception as e:
            self.stderr.write('Snitch Create Failure with e : ' + str(e))
