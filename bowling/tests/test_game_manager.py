from django.test import TestCase
from bowling.logic.game_manager import GameManager
from bowling.logic.frame import Frame


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

    def test_has_frames_dict_with_ten_frames(self):
        game_manager = GameManager()
        for index in range(1, 11):
            self.assertIsInstance(game_manager.frames[index], Frame)
            self.assertEqual(
                game_manager.frames[index].name,
                index
            )
