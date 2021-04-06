from django.test import TestCase
from bowling.logic.game_manager import GameManager


class TestGameManager(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_init_takes_game_id_creates_if_none_or_loads(self):
        game_manager = GameManager()
        game_manager_two = GameManager(game_manager.game.id)
        self.assertEqual(
            game_manager.game.id,
            game_manager_two.game.id,
            '\nFirst game manager should have created a new game, '
            'second one should have loaded that game.'
        )

