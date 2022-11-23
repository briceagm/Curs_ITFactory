import unittest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By

class Tema9(unittest.TestCase):

    def setUp(self) -> None:
        service = ChromeService(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=service)
        self.chrome.implicitly_wait(10)
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.maximize_window()
        time.sleep(2)


    def tearDown(self) -> None:
        self.chrome.quit()
#test1
    def test_form_authentication_button(self):
        form_authentication_btt = self.chrome.find_element(By.XPATH, '//*[text()="Form Authentication"]')
        form_authentication_btt.click()
        time.sleep(2)
        assert self.chrome_current_url == "https://the-internet.herokuapp.com/login"
        time.sleep(2)

    # def test_page_title(self):
    #     page_title = self.driver.find_element(By.TAG_NAME, "title")
    #     # print(page_title.text)
    #     # assert page_title.text == "The Internet", 'ceva nu merge'
    #     self.assertEqual(page_title.text, "The Internet", "URl-ul nu este cel dorit")
    #

    def test3(self):
        h2_element = self.chrome.find_element(By.TAG_NAME, "h2")
        assert h2_element.text == "Available Examples"

    def test_10(self):
        self.chrome.get('https://the-internet.herokuapp.com/login')
        username_input = self.chrome.find.element(By.ID, "username")
        username_input.send_keys("tomsmith")
        password_input = self.chrome.find_element(By.ID, "password")
        password_input.send_keys("SuperSecretPassword!")
        login_button = self.chrome.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        assert '/secure' in self.chrome.current_url
