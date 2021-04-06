from django.test import TestCase
from bowling.models.roll import Roll
from bowling.models.game import Game


class TestModels(TestCase):
    def test_roll_model_has_pins_hit(self):
        expected_pins_hit = 1
        roll = Roll.objects.create(pins_hit=expected_pins_hit)
        self.assertEqual(
            roll.pins_hit,
            expected_pins_hit
        )

    def test_game_model_has_base_parameters(self):
        game = Game.objects.create()
        self.assertEqual(
            game.current_frame,
            1  # should be default
        )
        self.assertEqual(
            game.active,
            True  # should be default
        )
