from bowling.logic.game_manager import GameManager


class GameStyle:

    def __init__(self, game_id=None):
        self.game_manager = GameManager(game_id)

    @staticmethod
    def get_headers():
        headers = {}
        for index in range(1, 12):
            headers[index] = index
        headers[11] = 'Total Score'
        return headers
