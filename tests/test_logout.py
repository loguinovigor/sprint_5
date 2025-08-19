import pytest
from pages.home_page import HomePage
from pages.auth_page import AuthModal
from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.data import EXISTING_EMAIL, EXISTING_PASSWORD

@pytest.mark.logout
def test_logout_user(driver, base_url):
    home = HomePage(driver)
    auth = AuthModal(driver)

    # Авторизация
    home.open_home(base_url)
    home.open_auth_modal()
    auth.open_login()
    auth.login(EXISTING_EMAIL, EXISTING_PASSWORD)
    assert home.is_logged_in(), "Не удалось авторизоваться для проверки логаута."

    # Логаут
    home.logout()

    # Проверяем, что теперь видна кнопка "Вход и регистрация"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.LOGIN_REGISTER_BUTTON))
