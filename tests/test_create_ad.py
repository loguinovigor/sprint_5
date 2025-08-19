import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.auth_page import AuthModal
from pages.create_ad_page import CreateAdPage
from pages.profile_page import ProfilePage
from locators import AuthModalLocators, LoginFormLocators
from utils.data import EXISTING_EMAIL, EXISTING_PASSWORD

@pytest.mark.create_ad
def test_create_ad_anonymous_shows_login_modal(driver, base_url):
    home = HomePage(driver)

    home.open_home(base_url)
    home.open_post_ad()

    # Ожидаем, что открылась модалка авторизации: видны поля email и пароль
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthModalLocators.MODAL))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginFormLocators.EMAIL_INPUT))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginFormLocators.PASSWORD_INPUT))

@pytest.mark.create_ad
def test_create_ad_authorized_success(driver, base_url):
    home = HomePage(driver)
    auth = AuthModal(driver)
    ad = CreateAdPage(driver)
    profile = ProfilePage(driver)

    # Логин
    home.open_home(base_url)
    home.open_auth_modal()
    auth.open_login()
    auth.login(EXISTING_EMAIL, EXISTING_PASSWORD)
    assert home.is_logged_in(), "Не удалось авторизоваться перед созданием объявления."

    # Создание объявления
    home.open_post_ad()
    title = "Автотестовый товар"
    description = "Описание, созданное автотестом."
    price = 12345
    ad.fill_form(title=title, description=description, price=price, category=None, city=None, condition="new")
    ad.publish()

    # Переходим в профиль (если есть ссылка)
    try:
        home.click(("xpath","//a[contains(@href,'profile') or .//span[normalize-space()='Профиль']]"))
    except Exception:
        pass

    profile.assert_ad_visible(title)
