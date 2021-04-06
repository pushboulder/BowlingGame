from django.test import TestCase, tag


class TestFullGameFlow(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.game_id = None
        cls.expected_scores = [
            20, 39, 48, 66,
            74, 84, 90, 120,
            148, 167
        ]
        cls.expected_rolls = [
            '', 'X', '7', '/', '9', '-',
            '', 'X', '-', '8', '8', '/',
            '-', '6', 'X', 'X', 'X', '8', '1'
        ]
        cls.rolls_to_make = [
            10, 7, 3, 9,
            0, 10, 0, 8,
            8, 2, 0, 6,
            10, 10, 10, 8, 1
        ]

    @tag('system')
    def test_game_can_be_created_updated_and_completed(self):
        response = self.client.post('/', {'game_id': 'create'})
        game_id = response.context.get('game_id', None)
        self.assertIsNotNone(
            game_id,
            'Expected a new game to be created and game_id to exist in response.'
        )
        for index in range(0, len(self.rolls_to_make)):
            response = self.get_roll_response(index, game_id)
            self.check_response(response, 'scores', self.expected_scores[0:index + 1])
            self.check_response(response, 'rolls', self.expected_rolls[0:index + 1])
        self.check_response(response, 'is_active', False)

    def get_roll_response(self, index, game_id):
        return self.client.get(
            '/{game_id}'.format(game_id=game_id),
            {
                'pins_hit': self.rolls_to_make[index]
            }
        )

    def check_response(self, response, target, expected):
        actual = response.context.get(target, None)
        self.assertEqual(
            actual,
            expected,
            'Expected {target} to match:\nActual: {actual}\nExpected: {expected}'.format(
                target=target,
                actual=actual,
                expected=expected
            )
        )

