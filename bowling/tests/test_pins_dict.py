from django.test import TestCase
from bowling.templatetags.pins_dict import pins_dict


class TestPinsDict(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.maxDiff = None

    def test_pins_dict_response(self):
        available_pins = {
            0: True, 1: True, 2: True, 3: True, 4: True, 5: True,
            6: True, 7: False, 8: False, 9: False, 10: False
        }
        expected = {
            0: [
                {'id': 0, 'disabled': ''}
            ],
            1: [
                {'id': 1, 'disabled': ''},
                {'id': 2, 'disabled': ''},
                {'id': 3, 'disabled': ''}
            ],
            2: [
                {'id': 4, 'disabled': ''},
                {'id': 5, 'disabled': ''},
                {'id': 6, 'disabled': ''}
            ],
            3: [
                {'id': 7, 'disabled': 'disabled'},
                {'id': 8, 'disabled': 'disabled'},
                {'id': 9, 'disabled': 'disabled'}
            ],
            4: [
                {'id': 10, 'disabled': 'disabled'}
            ]
        }

        actual = pins_dict(available_pins)
        self.assertEqual(
            actual,
            expected
        )
