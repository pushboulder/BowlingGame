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
        cls.game_style = GameStyle()
        cls.pins_hit_list = [10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1]

        available_pins_data = [11, 4, 11, 2, 11, 11, 11, 11, 3, 11, 11, 11, 11, 11, 11, 3, 0]
        cls.expected_available_pins = []
        for pins in available_pins_data:
            available_pins = {}
            for index in range(0, 11):
                available_pins[index] = index < pins
            cls.expected_available_pins.append(available_pins)

        for pins_hit in cls.pins_hit_list:
            cls.game_style.game_manager.roll(pins_hit)
        cls.expected_roll_results = [
            '', 'X', '7', '/', '9', '-',
            '', 'X', '-', '8', '8', '/',
            '-', '6', '', 'X', '', 'X',
            'X', '8', '1'
        ]
        cls.expected_scores = [
            20, 39, 48, 66,
            74, 84, 90, 120,
            148, 167
        ]
        cls.expected_current_frame_data = {
            'rolls_remaining': 0,
            'current_frame': 10,
            'available_pins': {
                0: False, 1: False, 2: False, 3: False, 4: False, 5: False,
                6: False, 7: False, 8: False, 9: False, 10: False
            }
        }
        cls.get_context_sections = [
            'headers', 'rolls', 'scores', 'rolls_remaining', 'current_frame', 'available_pins',
        ]

    @staticmethod
    def get_new_game_style(rolls_to_apply=None):
        game_style = GameStyle()
        if rolls_to_apply:
            for pins_hit in rolls_to_apply:
                game_style.game_manager.roll(pins_hit)
        return game_style

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
        self.assertEqual(
            self.game_style.get_headers(),
            self.expected_headers
        )

    def test_get_roll_results_returns_expected_data(self):
        self.assertEqual(
            self.game_style.get_roll_results(),
            self.expected_roll_results,
            '\nExpected: {}\nActual: {}'.format(
                self.game_style.get_roll_results(),
                self.expected_roll_results
            )
        )

    def test_partial_game_results(self):
        game_style = GameStyle()
        pins_hit_list = self.pins_hit_list[0:9]
        for pins_hit in pins_hit_list:
            game_style.game_manager.roll(pins_hit)

        roll_results = game_style.get_roll_results()
        expected = self.expected_roll_results[0:11]
        expected.extend([''] * 10)
        self.assertEqual(
            roll_results,
            expected,
            '\nExpected: {}\nActual:   {}'.format(
                roll_results,
                expected
            )
        )
        scores = game_style.get_scores()
        expected = self.expected_scores[0:5]
        self.assertEqual(
            scores,
            expected,
            '\nExpected: {}\nActual:   {}'.format(
                scores,
                expected,
            )
        )

    def test_get_scores_returns_expected_data(self):
        self.assertEqual(
            self.game_style.get_scores(),
            self.expected_scores
        )

    def test_get_current_frame_data_returns_expected_data(self):
        game_style = self.get_new_game_style(self.pins_hit_list)
        actual = game_style.get_current_frame_data()
        self.assertEqual(
            actual,
            self.expected_current_frame_data,
            '\nExpected: {}\nActual:   {}'.format(
                self.expected_current_frame_data,
                actual
            )
        )

    def test_get_available_pins_returns_expected_data(self):
        game_style = self.get_new_game_style()
        for index in range(0, len(self.pins_hit_list)):
            game_style.game_manager.roll(self.pins_hit_list[index])
            self.assertEqual(
                game_style.get_available_pins(),
                self.expected_available_pins[index]
            )

    def test_get_context_returns_expected_data_sections(self):
        game_style = self.get_new_game_style()
        actual = game_style.get_context()
        for section in self.get_context_sections:
            self.assertIsNotNone(
                actual.get(section, None)
            )
