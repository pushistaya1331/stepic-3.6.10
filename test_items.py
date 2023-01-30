import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    basket_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
    assert len(basket_button.text) > 0