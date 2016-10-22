import unittest
from selenium import webdriver


# Firefox does not work, not fully installed..

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        # Edith has heard of a great website on to to lists and goes to homepage
        self.browser.get('http://localhost:8000')

        # She notices the header mentions to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a do-do right away

        # She types "Buy peacock feathers" into a to-do

        # When she hits enter,  the page updates and lists "1. Buy peacock feathers"

        # There is still a text box inviting her to enter another to-do

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list.  She sees there is a
        # unique url for her

        # She visits that url and her list is still there

        # Satisfied, she goes to sleep

if __name__ == '__main__':
    unittest.main()
