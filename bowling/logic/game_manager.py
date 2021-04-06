from bowling.models.game import Game
from bowling.logic.frame import Frame


class GameManager:
    game = None
    frames = {}

    def __init__(self, game_id=None):
        self.set_game(game_id)
        self.set_frames()

    def set_game(self, game_id):
        if game_id is None:
            self.create_game()
        else:
            self.game = Game.objects.get(id=game_id)

    def create_game(self):
        self.game = Game.objects.create()

    def set_frames(self):
        for index in range(1, 11):
            self.frames[index] = Frame(index)
