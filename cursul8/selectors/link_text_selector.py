"""
<a class="navbar-brand" id="logo" href="/">Formy</a>
UN tag de tip a(anchor) este folosit pentru link-uri
Acesta trebuie sa aiba in mod obligatoriu un atribut numit href(hyperreference), care reprezinta locatia pe care ne va duce linkul.

Putem selecta un tag de tip a, folosind LINK_TEXT sau PARTIAL.LINK_TEXT.

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
formy_link = chrome.find_element(By.LINK_TEXT, "FORMY")
formy_link.click()
print(chrome.current_url)
assert chrome.current_url == "https://formy-project.herokuapp.com/"
time.sleep(2)

drag_and_drop_link = chrome.find_element(By.PARTIAL_LINK_TEXT, "Drag")
drag_and_drop_link.click()
time.sleep(2)

h1 = chrome.find_element(By.TAG_NAME, "h1")
assert h1.text == "Drag the image into the box"
