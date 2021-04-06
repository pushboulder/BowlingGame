from django.test import TestCase
from bowling.logic.game_manager import GameManager
from bowling.logic.game_style import GameStyle


class TestGameStyle(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.expected_headers = {
            1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6,
            7: 7, 8: 8, 9: 9, 10: 10, 11: 'Total Score'
        }

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

    def test_get_headers_returns_expected_data(self):
        game_style = GameStyle()
        self.assertEqual(
            game_style.get_headers(),
            self.expected_headers
        )
