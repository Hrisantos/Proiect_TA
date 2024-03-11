"""
In this file we have all search locators for our tests.
"""
from selenium.webdriver.common.by import By


class PageLocators:

    cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    search_bar = (By.CSS_SELECTOR, "input[type='text']")
    search_button = (By.CSS_SELECTOR, "button[type='submit'][title='Cauta']")
    account_button = (By.CSS_SELECTOR, "span[class='jsx-9d04a24ff8b4af87 truncate hidden sm:block leading-18.2 -tracking-0.29']")
    email_field = (By.CSS_SELECTOR, "input[label='Introdu adresa de email']")
    password_field = (By.CSS_SELECTOR, "input[type='password']")
    login_button = (By.XPATH, "//span[text()='Autentificare']")
    register_button = (By.XPATH, "//a[text()='Inregistrare']")
    password_recovery = (By.XPATH, "//a[text()='Recuperare parola']")
    cart_button = (By.XPATH, "//span[text()='Cosul meu']")
