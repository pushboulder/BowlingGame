from django.test import TestCase
from bowling.logic.views import get_context, get_template


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.template_data = [
            {'game_id': 1, 'expected': 'game.html'},
            {'game_id': 'create', 'expected': 'game.html'},
            {'game_id': None, 'expected': 'base.html'}
        ]
        cls.context_data = [
            {
                'game_id': 'create',
                'pins_hit': None,
                'expected': {
                    'rolls': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    'rolls_remaining': 2,
                    'available_pins': {
                        0: True, 1: True, 2: True, 3: True, 4: True, 5: True,
                        6: True, 7: True, 8: True, 9: True, 10: True
                    }
                }
            },
            {
                'game_id': 1,
                'pins_hit': 3,
                'expected': {
                    'rolls': ['3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                    'rolls_remaining': 1,
                    'available_pins': {
                        0: True, 1: True, 2: True, 3: True, 4: True, 5: True,
                        6: True, 7: True, 8: False, 9: False, 10: False
                    }
                }
            }
        ]

    def test_get_template_returns_appropriate_template(self):
        for data in self.template_data:
            actual = get_template(data['game_id'])
            self.assertEqual(
                actual,
                data['expected']
            )

    def test_get_context_returns_empty_without_game_id(self):
        actual = get_context(None, 5)
        self.assertEqual(
            actual,
            {}
        )

    def test_get_context_returns_appropriate_template(self):
        for data in self.context_data:
            actual = get_context(data['game_id'], data['pins_hit'])
            for key, value in data['expected'].items():
                self.assertEqual(
                    actual[key],
                    value
                )

    def test_view_sends_context_and_template_through_render(self):
        for data in self.context_data:
            context = {'game_id': data['game_id']}
            url = '' if context['game_id'] == 'create' else context['game_id']
            if data['pins_hit']:
                context['pins_hit'] = data['pins_hit']
            response = self.client.post('/{}'.format(url), context)
            templates = [t.name for t in response.templates]
            self.assertIn(
                'game.html',
                templates
            )
            for key, value in data['expected'].items():
                self.assertEqual(
                    response.context[key],
                    value
                )
