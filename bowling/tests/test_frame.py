from django.test import TestCase
from bowling.logic.frame import Frame


class TestFrame(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.defaults = {
            'max_pin_sets': 1,
            'pin_sets': [],
            'score': 0,
            'name': 1
        }
        cls.max_pin_sets_data = {
            1: 1, 2: 1, 3: 1, 4: 1, 5: 1,
            6: 1, 7: 1, 8: 1, 9: 1, 10: 3
        }

    def test_frame_takes_one_arg_has_expected_defaults(self):
        frame = Frame(self.defaults['name'])
        self.assertEqual(
            {
                'max_pin_sets': frame.max_pin_sets,
                'pin_sets': frame.pin_sets,
                'score': frame.score,
                'name': frame.name
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
