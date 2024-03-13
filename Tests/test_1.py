"""
TEST if is the correct website
"""
import unittest
from selenium import webdriver
from Page_data_locators.page_data import PageData
from Core_code.core_page import CorePage
from Base.base_page import BasePage


class TestSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_open(self):
        main_page = CorePage(self.driver)
        cookies = CorePage(self.driver)
        actual_url = BasePage(self.driver)
        page_url = PageData.page_url

        main_page.open_site()
        cookies.accept_cookies()

        assert actual_url.get_current_url() == page_url, f'Unexpected URL'
        print("PASS")
