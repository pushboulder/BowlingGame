from django.test import TestCase
from bowling.logic.frame import Frame


class TestFrame(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.defaults = {
            'max_pin_sets': 1,
            'pin_sets': 1,
            'score': 0,
            'name': 1,
            'remaining_rolls': 2
        }
        cls.max_pin_sets_data = {
            1: 1, 2: 1, 3: 1, 4: 1, 5: 1,
            6: 1, 7: 1, 8: 1, 9: 1, 10: 3
        }
        cls.max_rolls_data = [
            {'name': 1, 'rolls': [2, 8, 10, 10], 'pins_hit': [2, 8], 'pin_set_count': 1},
            {'name': 10, 'rolls': [2, 8, 10, 10], 'pins_hit': [2, 8, 10], 'pin_set_count': 2},
            {'name': 10, 'rolls': [10, 0, 10, 8], 'pins_hit': [10, 0, 10], 'pin_set_count': 2},
            {'name': 10, 'rolls': [10, 10, 6, 4], 'pins_hit': [10, 10, 6], 'pin_set_count': 3},
            {'name': 10, 'rolls': [2, 7, 6, 4], 'pins_hit': [2, 7], 'pin_set_count': 1}
        ]
        cls.is_complete_data = [
            {'name': 1, 'rolls': [10], 'is_complete': True},
            {'name': 1, 'rolls': [4, 6], 'is_complete': True},
            {'name': 1, 'rolls': [5], 'is_complete': False},
            {'name': 1, 'rolls': [], 'is_complete': False},
            {'name': 10, 'rolls': [10, 10, 10], 'is_complete': True},
            {'name': 10, 'rolls': [10, 3, 7], 'is_complete': True},
            {'name': 10, 'rolls': [0, 2], 'is_complete': True},
            {'name': 10, 'rolls': [0, 10, 4], 'is_complete': True},
            {'name': 10, 'rolls': [6], 'is_complete': False},
            {'name': 10, 'rolls': [10], 'is_complete': False},
            {'name': 10, 'rolls': [], 'is_complete': False},
        ]
        cls.calculate_score_data = [
            {'name': 1, 'rolls': [6], 'add_rolls': [10, 10], 'score': 0},
            {'name': 1, 'rolls': [5, 5], 'add_rolls': [10, 10], 'score': 20},
            {'name': 1, 'rolls': [10], 'add_rolls': [10, 10], 'score': 30},
            {'name': 1, 'rolls': [2, 4], 'add_rolls': [10, 10], 'score': 6},
            {'name': 1, 'rolls': [10], 'add_rolls': [10], 'score': 0},
            {'name': 1, 'rolls': [10], 'add_rolls': [10, 10], 'score': 30},
            {'name': 10, 'rolls': [5, 5], 'add_rolls': [10, 10], 'score': 0},
            {'name': 10, 'rolls': [10, 5], 'add_rolls': [10, 10], 'score': 0},
            {'name': 10, 'rolls': [10, 10], 'add_rolls': [10, 10], 'score': 0},
            {'name': 10, 'rolls': [10, 10, 10], 'add_rolls': [10, 10], 'score': 30},
            {'name': 10, 'rolls': [8, 2, 3], 'add_rolls': [10, 10], 'score': 13},
            {'name': 10, 'rolls': [5, 3], 'add_rolls': [10, 10], 'score': 8},
        ]

    def test_frame_takes_one_arg_has_expected_defaults(self):
        frame = Frame(self.defaults['name'])
        self.assertEqual(
            {
                'max_pin_sets': frame.max_pin_sets,
                'pin_sets': len(frame.pin_sets),
                'score': frame.score,
                'name': frame.name,
                'remaining_rolls': frame.remaining_rolls
            },
            self.defaults
        )

    def test_max_pin_sets_changes_if_name_is_ten(self):
        for name, max_pin_sets in self.max_pin_sets_data.items():
            frame = Frame(name)
            self.assertEqual(
                frame.max_pin_sets,
                max_pin_sets
            )

    def test_roll_method_adds_pins_if_incomplete(self):
        for name in range(1, 11):
            frame = Frame(name)
            for pins_hit in [10, 10, 10, 10]:
                frame.roll(pins_hit)
            self.assertEqual(
                len(frame.pin_sets),
                frame.max_pin_sets
            )

    def test_roll_method_has_remaining_rolls_increases_once_on_pin_set_add(self):
        for data in self.max_rolls_data:
            frame = Frame(data['name'])
            for roll in data['rolls']:
                frame.roll(roll)

            pins_hit = []
            for pin_set in frame.pin_sets:
                pins_hit.extend(pin_set.rolls)
            self.assertEqual(
                pins_hit,
                data['pins_hit'],
                '\nData used in this test: {}'.format(data)
            )
            self.assertEqual(
                len(frame.pin_sets),
                data['pin_set_count'],
                '\nData used in this test: {}'.format(data)
            )

    def test_is_complete_method_shows_when_a_frame_has_ended(self):
        for data in self.is_complete_data:
            frame = Frame(data['name'])
            for roll in data['rolls']:
                frame.roll(roll)
            self.assertEqual(
                frame.is_complete(),
                data['is_complete'],
                '\nChecking is_complete with this data: {}'.format(data)
            )

    def test_calculate_score_method_returns_zero_unless_complete(self):
        for data in self.calculate_score_data:
            frame = Frame(data['name'])
            for roll in data['rolls']:
                frame.roll(roll)
            score = frame.calculate_score(data['add_rolls'])
            self.assertEqual(
                [score, frame.score],
                [data['score'], data['score']]
            )
