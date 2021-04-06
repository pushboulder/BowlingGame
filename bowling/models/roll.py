from django.db import models


class Roll(models.Model):
    pins_hit = models.SmallIntegerField()
