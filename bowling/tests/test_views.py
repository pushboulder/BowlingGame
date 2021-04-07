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
