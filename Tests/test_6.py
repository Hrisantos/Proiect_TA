"""
TEST search for an unlisted product
"""
import unittest
from selenium import webdriver
from Core_code.core_page import CorePage
from Page_data_locators.page_data import PageData


class UnlistedProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_unlisted_product(self):
        main_page = CorePage(self.driver)
        cookies = CorePage(self.driver)
        unlisted_prod = CorePage(self.driver)

        main_page.open_site()
        cookies.accept_cookies()
        missing_prod = unlisted_prod.product_not_found()

        assert missing_prod.text == PageData.missing_text, f"Message is {missing_prod.text}"
        print("PASS")
