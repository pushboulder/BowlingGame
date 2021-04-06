from django.test import TestCase
from bowling.logic.pin_set import PinSet


class TestPinSet(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.expected_rolls = []
        cls.expected_max_rolls = 2

    def test_pin_set_has_default_values(self):
        pin_set = PinSet()
        self.assertEqual(
            pin_set.rolls,
            self.expected_rolls
        )
        self.assertEqual(
            pin_set.max_rolls,
            self.expected_max_rolls
        )