from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        response = home_page(request)

        # Earlier tests from before we moved to a template
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do List</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))

        # Tests the home page uses the home.html template
        expected_content = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_content)

        # No longer works when csrf_token in template
        with open('lists/templates/home.html') as f:
            expected_content = f.read()
        self.assertEqual(response.content.decode(), expected_content)
