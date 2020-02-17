from selenium import webdriver
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
        self.fail('Finish the tests')

if __name__ == '__main__':
    unittest.main(warnings='ignore')