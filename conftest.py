import os
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from src.helpers import BASE_URL
from src.locators import MainPageLocators, LoginForm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver: WebDriver):
    driver.get(BASE_URL)
    # легкое явное ожидание вместо implicit/sleep
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.LOGGIN_BUTTON)
    )
    return driver

