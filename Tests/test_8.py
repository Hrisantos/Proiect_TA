"""
TEST account and connect button error
"""
import unittest
from selenium import webdriver
from Core_code.core_page import CorePage
from Page_data_locators.page_data import PageData


class LoginErrorMsg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_error_msg(self):
        login_test_error_msg = CorePage(self.driver)

        login_test_error_msg.open_site()
        login_test_error_msg.accept_cookies()
        login_test_error_msg.second_connect_button()
        email_msg = login_test_error_msg.get_email_message()
        pw_msg = login_test_error_msg.get_pw_message()

        assert email_msg == PageData.email_error_msg, "Not expected"
        assert pw_msg == PageData.pw_error_msg, "Not expected"
        print("PASS")
