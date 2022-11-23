from selenium.webdriver.common.by import By


class LoginPage:

    URL = 'https://www.saucedemo.com/'
    USERNAME_SELECTOR = (By.ID, 'user-name')
    PASSWORD_SELECTOR = (By.ID, 'password')
    LOGIN_BUTTON_SELECTOR = (By.ID, 'login-button')

    def __init__(self, browser):
        self.driver.get