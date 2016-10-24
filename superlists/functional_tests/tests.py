import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  django.test import LiveServerTestCase


# Firefox does not work, not fully installed..

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)  # To avoid issues if browser can't keep up with tests

    def tearDown(self):
        self.browser.quit()

    # Helper method
    def check_for_row_in_list_table(self, expected_row):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            expected_row,
            [row.text for row in rows]
        )

    def test_starting_a_new_todo_list(self):
        # Edith has heard of a great website on to to lists and goes to homepage
        self.browser.get(self.live_server_url)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # She notices the header mentions to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a do-do right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peacock feathers" into a to-do
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates and lists "1. Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        # import time
        # time.sleep(10)

        self.check_for_row_in_list_table("1: Buy peacock feathers")


        # There is still a text box inviting her to enter another to-do
        # She enters "Use feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table("2: Use feathers to make a fly")
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # Edith wonders whether the site will remember her list.  She sees there is a
        # unique url for her
        self.fail('Finish the test')

        # She visits that url and her list is still there

        # Satisfied, she goes to sleep


if __name__ == '__main__':
    unittest.main()
