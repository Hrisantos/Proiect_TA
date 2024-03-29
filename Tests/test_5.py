"""
TEST highest price product
"""
import unittest
from selenium import webdriver
from Core_code.core_page import CorePage


class TestHighProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_high_product(self):
        main_page = CorePage(self.driver)
        cookies = CorePage(self.driver)
        search_product = CorePage(self.driver)
        high_price = CorePage(self.driver)

        main_page.open_site()
        cookies.accept_cookies()
        search_product.execute_find_product()
        highest_product_price = high_price.get_high_prices()

        self.assertIsInstance(highest_product_price, float, "Product price with the highest price is not a string")
        print("PASS")
