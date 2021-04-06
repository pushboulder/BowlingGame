from django.test import TestCase
from bowling.logic.game_manager import GameManager
from bowling.logic.frame import Frame


class TestGameManager(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.roll_current_frame = [
            {'frame': 1, 'roll': 1, 'expect': [1]},
            {'frame': 1, 'roll': 9, 'expect': [1, 9]},
            {'frame': 2, 'roll': 10, 'expect': [10]},
            {'frame': 3, 'roll': 0, 'expect': [0]},
            {'frame': 3, 'roll': 8, 'expect': [0, 8]},
        ]

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

    def test_roll_method_updates_game_current_frame(self):
        game_manager = GameManager()
        for data in self.roll_current_frame:
            game_manager.game.current_frame = data['frame']
            game_manager.roll(data['roll'])
            self.assertEqual(
                game_manager.frames[data['frame']].pin_sets[0].rolls,
                data['expect']
            )
