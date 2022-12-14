"""
Selenium- librarie de python care ne ajuta sa interactionam cu o pagina web/HTML.
1. OBtinem un driver de browser(intr-o variabila)
2. Luam cu find_element/ find_elements elementele de care avem nevoie
3. Interactionam cu ele folosind metodele disponibile
4. Facem assert.

"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://formy-project.herokuapp.com/form")
time.sleep(2)
# selectori dupa ID
first_name_input = chrome.find_element(by=By.ID, value="first-name")
first_name_input.send_keys("Marcela")
time.sleep(2)

last_name_input = chrome.find_element(By.ID, "last-name")
last_name_input.send_keys("Briceag")
time.sleep(2)