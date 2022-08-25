import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import unittest


class NewUserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver4FirefoxBrowser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def tearDown(self) -> None:
        self.driver4FirefoxBrowser.quit()

    def test_can_enter_two_numbers_and_get_sum(self):
        self.driver4FirefoxBrowser.get('http://localhost:8000')
        self.assertIn('Calculator',self.driver4FirefoxBrowser.title)
        self.fail('Complete the test')

if __name__ == '__main__'        :
    unittest.main()
