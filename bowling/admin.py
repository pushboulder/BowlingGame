from django.contrib import admin
from bowling.models.roll import Roll
from bowling.models.game import Game
from bowling.models.game_roll import GameRoll


admin.site.register(Roll)
admin.site.register(Game)
admin.site.register(GameRoll)
