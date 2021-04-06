from django.test import TestCase
from bowling.logic.pin_set import PinSet
from bowling.models.roll import Roll


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

    def test_roll_method_adds_to_roll_list_until_max(self):
        roll = Roll.objects.create(pins_hit=3)
        pin_set = PinSet()
        for _ in range(0, pin_set.max_rolls + 1):
            pin_set.roll(roll)
        self.assertEqual(
            pin_set.rolls,
            [roll, roll]
        )
