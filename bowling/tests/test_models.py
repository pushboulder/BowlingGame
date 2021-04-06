from django.test import TestCase
from bowling.models.roll import Roll


class TestModels(TestCase):
    def test_roll_model_has_pins_hit(self):
        expected_pins_hit = 1
        roll = Roll.objects.create(pins_hit=expected_pins_hit)
        self.assertEqual(
            roll.pins_hit,
            expected_pins_hit
        )
