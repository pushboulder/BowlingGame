from django.db import models


class Game(models.Model):
    current_frame = models.SmallIntegerField(
        default=1
    )
    active = models.BooleanField(
        default=True
    )
