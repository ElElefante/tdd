from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        # Ensure that page is loaded before test starts (may be more then 3 secs)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_and_retrieve_it_later(self):
        # User starts the application
        self.browser.get('http://localhost:8000')
        # Did the desired application start correctly?
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # Enter To-Do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.__getattribute__('placeholder'),
            'Enter a To-Do item'
        )
        # Typing an item
        inputbox.send_keys('Buy peacock feathers')
        # Terminate by pressing Enter
        inputbox.send_keys(Keys.Enter)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        self.fail('Finish the tests')

if __name__ == '__main__':
    unittest.main(warnings='ignore')