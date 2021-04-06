from bowling.models.game import Game


class GameManager:
    game = None

    def __init__(self, game_id=None):
        self.set_game(game_id)

    def set_game(self, game_id):
        if game_id is None:
            self.create_game()
        else:
            self.game = Game.objects.get(id=game_id)

    def create_game(self):
        self.game = Game.objects.create()
