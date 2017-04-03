import unittest
from selenium import webdriver


class FirstTest(unittest.TestCase):
    def setUp(self):
        # creates a new Chrome session
        self.driver = webdriver.Chrome()
        # maximizes windows
        self.driver.maximize_window()

    def test_first_selenium_test(self):
        self.driver.get("http://www.swtestacademy.com")

    def tearDown(self):
        # closes the Chrome session
        self.driver.quit()