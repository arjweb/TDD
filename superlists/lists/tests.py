from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        response = home_page(request)

        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do List</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))

        # Tests the home page uses the home.html template
        with open('lists/templates/home.html') as f:
            expected_content = f.read()
        self.assertEqual(response.content.decode(), expected_content)


