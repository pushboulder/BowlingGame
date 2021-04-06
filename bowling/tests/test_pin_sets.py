from django.test import TestCase
from bowling.logic.pin_set import PinSet


class TestPinSet(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.expected_rolls_default = []
        cls.expected_max_rolls_default = 2
        cls.expected_rolls = [3, 3]
        cls.get_status_data = [
            {'pins_hit': [0, 1], 'expected_status': 'Complete'},
            {'pins_hit': [4], 'expected_status': 'Incomplete'},
            {'pins_hit': [10], 'expected_status': 'Strike'},
            {'pins_hit': [2, 8], 'expected_status': 'Spare'}
        ]

    def test_pin_set_has_default_values(self):
        pin_set = PinSet()
        self.assertEqual(
            pin_set.rolls,
            self.expected_rolls_default
        )
        self.assertEqual(
            pin_set.max_rolls,
            self.expected_max_rolls_default
        )

    def test_roll_method_adds_to_roll_list_until_max(self):
        pin_set = PinSet()
        for _ in range(0, pin_set.max_rolls + 1):
            pin_set.roll(3)
        self.assertEqual(
            pin_set.rolls,
            self.expected_rolls
        )

    def test_get_status_returns_expected(self):
        for data in self.get_status_data:
            pin_set = PinSet()
            for pins_hit in data['pins_hit']:
                pin_set.roll(pins_hit)
            actual_status = pin_set.get_status()
            self.assertEqual(
                actual_status,
                data['expected_status']
            )
