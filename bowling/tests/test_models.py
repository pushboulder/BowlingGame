from django.test import TestCase
from bowling.models.roll import Roll
from bowling.models.game import Game
from bowling.models.game_roll import GameRoll


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.expected_pins_hit = 2
        cls.roll = Roll.objects.get(
            pins_hit=cls.expected_pins_hit
        )
        cls.game = Game.objects.create()
        cls.game_current_frame_default = 1
        cls.game_active_default = True

    def test_roll_model_has_pins_hit(self):
        self.assertEqual(
            self.roll.pins_hit,
            self.expected_pins_hit
        )

    def test_game_model_has_base_parameters(self):
        game = Game.objects.create()
        self.assertEqual(
            game.current_frame,
            self.game_current_frame_default
        )
        self.assertEqual(
            game.active,
            self.game_active_default
        )

    def test_game_roll_model_has_foreign_keys(self):
        game_roll = GameRoll.objects.create(
            game=self.game,
            roll=self.roll
        )
        self.assertEqual(
            game_roll.game,
            self.game
        )
        self.assertEqual(
            game_roll.roll,
            self.roll
        )
