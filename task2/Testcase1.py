import unittest
from singleton import WebDriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestSteam(unittest.TestCase):
    driver = WebDriver().driver

    def setUp(self):
        self.driver.get("https://store.steampowered.com/")

    def test_main_page_steam(self):
        pass

    def tearDown(self):
        WebDriverWait(self.driver, 5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()