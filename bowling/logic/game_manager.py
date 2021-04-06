from bowling.models.game import Game
from bowling.models.game_roll import GameRoll
from bowling.models.roll import Roll
from bowling.logic.frame import Frame


class GameManager:
    def __init__(self, game_id=None):
        self.game = self.get_game(game_id)
        self.frames = self.get_frames()
        self.game_rolls = self.get_game_rolls()
        self.update_frames()

    def get_game(self, game_id):
        if game_id is None:
            return self.create_game()
        return self.load_game(game_id)

    @staticmethod
    def load_game(game_id):
        return Game.objects.get(id=game_id)

    @staticmethod
    def create_game():
        return Game.objects.create()

    @staticmethod
    def get_frames():
        frames = {}
        for index in range(1, 11):
            frames[index] = Frame(index)
        return frames

    def get_game_rolls(self):
        game_rolls = []
        for game_roll in GameRoll.objects.filter(game__id=self.game.id):
            game_rolls.append(game_roll)
        return game_rolls

    def roll(self, pins_hit):
        self.update_frame(pins_hit)
        self.add_game_roll(pins_hit)

    def update_frames(self):
        for game_roll in self.game_rolls:
            self.update_frame(game_roll.roll.pins_hit)

    def update_frame(self, pins_hit):
        self.frames[self.game.current_frame].roll(pins_hit)
        if self.frames[self.game.current_frame].is_complete():
            self.game.current_frame += 1
            self.game.save()

    def add_game_roll(self, pins_hit):
        game_roll = GameRoll.objects.create(
            game=self.game,
            roll=Roll.objects.get(pins_hit=pins_hit)
        )
        self.game_rolls.append(game_roll)


