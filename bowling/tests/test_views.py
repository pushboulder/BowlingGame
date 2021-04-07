from django.test import TestCase


class TestViews(TestCase):
    def test_view_returns_base_html_if_no_game_id_given(self):
        response = self.client.get('')
        expected = ['base.html', 'game_css.html', 'new_game.html']
        actual = []
        for template in response.templates:
            actual.append(template.name)
        self.assertEqual(
            actual,
            expected
        )

    def test_sending_create_returns_game_id(self):
        response = self.client.post('', {'game_id': 'create'})
        expected = 1
        actual = response.context.get('game_id', None)
        self.assertEqual(
            actual,
            expected
        )

    def test_sending_pins_hit_updates_rolls_context(self):
        response = self.client.post('', {'game_id': 'create'})
        game_id = response.context.get('game_id', None)
        response = self.client.post('/1', {'game_id': game_id, 'pins_hit': 3})
        expected = '3'
        actual = response.context.get('rolls', [None])
        self.assertEqual(
            actual[0],
            expected
        )