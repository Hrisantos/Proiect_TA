"""
TEST if one product have more than 5 items
"""
import unittest
from selenium import webdriver
from Page_data_locators.page_data import PageData
from Core_code.core_page import CorePage


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product(self):
        main_page = CorePage(self.driver)
        cookies = CorePage(self.driver)
        items = PageData.all_items
        search_product = CorePage(self.driver)
        all_products = CorePage(self.driver)

        main_page.open_site()
        cookies.accept_cookies()
        search_product.execute_find_product()
        result = all_products.execute_get_all_products()

        self.assertGreater(result, items, "Not as expected!")
        print("PASS")
