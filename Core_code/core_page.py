"""
In this file we will find all methods for testing our site.
"""
import time
from Base.base_page import BasePage
from Page_data_locators.page_locators import PageLocators
from Page_data_locators.page_data import PageData


class CorePage(BasePage):

    def open_site(self):
        self.open_url(PageData.page_url)

    def accept_cookies(self):
        self.click(PageLocators.cookies)

    def execute_find_product(self):
        self.type_text(PageLocators.search_bar, PageData.product_name)
        self.click(PageLocators.search_button)

    def execute_get_all_products(self):
        time.sleep(3)
        products = self.find_more_elements(PageLocators.get_products)
        if len(products) >= 5:
            return len(products)
        else:
            return len(products)

    def get_all_prices(self):
        time.sleep(3)
        name_element = self.find_more_elements(PageLocators.get_products_name)
        time.sleep(3)
        price_element = self.find_more_elements(PageLocators.get_product_price)

        name_key = []
        price_value = []

        for price in price_element:
            price_value.append(price.text)

        for name in name_element:
            name_key.append(name.text)

        dictionary_result = dict(zip(name_key, price_value))
        print(dictionary_result)

        lowest_key = min(dictionary_result, key=lambda k: dictionary_result[k])
        return lowest_key, dictionary_result[lowest_key]

    def get_high_prices(self):
        time.sleep(3)
        name_element = self.find_more_elements(PageLocators.get_products_name)
        time.sleep(3)
        price_element = self.find_more_elements(PageLocators.get_product_price)

        name_key = []
        price_value = []

        for price in price_element:
            price_value.append(price.text)

        for name in name_element:
            name_key.append(name.text)

        dictionary_result = dict(zip(name_key, price_value))
        print(dictionary_result)

        highest_key = max(dictionary_result, key=lambda k: dictionary_result[k])
        return highest_key, dictionary_result[highest_key]

    def first_connect_button(self):
        self.click(PageLocators.login_button)
        self.wait_for_clickable_element(PageLocators.connect_button)
        self.click(PageLocators.connect_button)

    def second_connect_button(self):
        self.click(PageLocators.login_button)
        self.wait_for_clickable_element(PageLocators.connect_button)
        self.click(PageLocators.connect_button)
        self.click(PageLocators.login_execute)

    def add_input(self):
        self.type_text(PageLocators.email_field, PageData.invalid_username_aron)
        self.type_text(PageLocators.password_field, PageData.invalid_password)
        self.click(PageLocators.login_execute)

    def add_correct_input(self):
        self.type_text(PageLocators.email_field, PageData.valid_email)
        self.type_text(PageLocators.password_field, PageData.valid_pw)
        self.click(PageLocators.login_execute)
        time.sleep(5)

    def clear_username(self):
        self.clear_text(PageLocators.email_field)
        self.type_text(PageLocators.email_field, PageData.invalid_username)
        time.sleep(5)

    def product_not_found(self):
        self.type_text(PageLocators.search_bar, PageData.unlisted_prod)
        self.click(PageLocators.search_button)

        return self.find(PageLocators.not_found)

    def get_error_message(self):
        return self.get_text(PageLocators.login_fail)

    def get_login_page_url(self):
        return self.get_current_url()

    def is_submit_button_shown(self):
        return self.is_object_displayed(PageLocators.login_execute)

    def is_enable(self):
        return self.is_object_enabled(PageLocators.login_execute)

    def get_email_message(self):
        return self.get_text(PageLocators.enter_email)

    def get_pw_message(self):
        return self.get_text(PageLocators.enter_password)
