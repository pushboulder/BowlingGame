from django.test import TestCase


class TestFrame(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.defaults = {
            'max_pin_sets': 1,
            'pin_sets': [],
            'score': 0,
            'name': 1
        }

    def test_frame_takes_one_arg_has_expected_defaults(self):
        frame = Frame(self.defaults['name'])
        self.assertEqual(
            {
                'max_pin_sets': frame.max_pin_sets,
                'pin_sets': frame.pin_sets,
                'score': frame.score,
                'name': frame.name
            }
        )
