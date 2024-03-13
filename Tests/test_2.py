"""
TEST if is the correct website title
"""
import unittest
from selenium import webdriver
from Page_data_locators.page_data import PageData
from Core_code.core_page import CorePage
from Base.base_page import BasePage


class TestTitle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        main_page = CorePage(self.driver)
        cookies = CorePage(self.driver)
        actual_title = BasePage(self.driver)
        page_title = PageData.page_title

        main_page.open_site()
        cookies.accept_cookies()

        assert actual_title.get_title() == page_title, f'Unexpected Page Title'
        print("PASS")

