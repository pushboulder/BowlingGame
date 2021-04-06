from django.contrib import admin
from bowling.models.roll import Roll
from bowling.models.game import Game


admin.site.register(Roll)
admin.site.register(Game)
