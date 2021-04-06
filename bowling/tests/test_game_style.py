from django.test import TestCase
from bowling.logic.game_manager import GameManager
from bowling.logic.game_style import GameStyle


class TestGameStyle(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_takes_game_id_creates_game_manager(self):
        game_style = GameStyle()
        self.assertIsInstance(
            game_style.game_manager,
            GameManager
        )
        game_style_two = GameStyle(game_style.game_manager.game.id)
        self.assertIsInstance(
            game_style_two.game_manager,
            GameManager
        )
