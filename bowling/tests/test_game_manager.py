from django.test import TestCase
from bowling.logic.game_manager import GameManager
from bowling.logic.frame import Frame
from bowling.models.game_roll import GameRoll
from bowling.models.roll import Roll


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
        cls.frame_score_data = {
            'rolls': [10, 10, 5, 5, 5, 5, 10, 10, 5, 5, 5, 5, 10, 10, 10, 10],
            'scores': [25, 20, 15, 20, 25, 20, 15, 20, 30, 30]
        }

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

    def test_has_game_rolls_which_updates_on_roll_or_load(self):
        game_manager = GameManager()
        expected = [0, 5, 10]
        for pins_hit in expected:
            game_manager.roll(pins_hit)
        self.assertEqual(
            game_manager.get_pins_hit_list(),
            expected
        )
        game_manager_two = GameManager(game_manager.game.id)

        self.assertEqual(
            game_manager_two.get_pins_hit_list(),
            expected
        )

    def test_calculate_score_updates_all_frames(self):
        game_manager = GameManager()
        for roll in self.frame_score_data['rolls']:
            game_manager.roll(roll)

        game_manager.calculate_score()

        for name, frame in game_manager.frames.items():
            self.assertEqual(
                frame.score,
                self.frame_score_data['scores'][name - 1]
            )

    def test_game_marked_inactive_when_all_frames_complete(self):
        game_manager = GameManager()
        for roll in self.frame_score_data['rolls']:
            game_manager.roll(roll)
        self.assertFalse(
            game_manager.game.active
        )
        complete_rolls = game_manager.get_pins_hit_list()
        game_manager.roll(10)
        extra_rolls = game_manager.get_pins_hit_list()
        self.assertEqual(
            complete_rolls,
            extra_rolls,
            '\nNo extra rolls should be recorded if a game is not active.'
        )
