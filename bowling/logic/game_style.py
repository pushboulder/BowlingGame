from bowling.logic.game_manager import GameManager


class GameStyle:

    def __init__(self, game_id=None):
        self.game_manager = GameManager(game_id)
