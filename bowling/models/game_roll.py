from django.db import models
from bowling.models.game import Game
from bowling.models.roll import Roll


class GameRoll(models.Model):
    game = models.ForeignKey(
        to=Game,
        on_delete=models.CASCADE
    )
    roll = models.ForeignKey(
        to=Roll,
        on_delete=models.CASCADE
    )
