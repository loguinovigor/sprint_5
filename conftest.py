import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def base_url():
    return "https://qa-desk.stand.praktikum-services.ru/"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1280,900")
    # options.add_argument("--headless=new")  # при необходимости
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(40)
    try:
        yield driver
    finally:
        driver.quit()
