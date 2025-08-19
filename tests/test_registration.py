import pytest
from pages.home_page import HomePage
from pages.auth_page import AuthModal
from utils.generators import unique_email
from utils.data import NEW_USER_NAME, VALID_PASSWORD

@pytest.mark.registration
def test_register_user_success(driver, base_url):
    home = HomePage(driver)
    auth = AuthModal(driver)

    home.open_home(base_url)
    home.open_auth_modal()
    auth.open_register()

    email = unique_email()
    auth.register(NEW_USER_NAME, email, VALID_PASSWORD)

    # Ожидаем переход на главную и отображение аватара и имени User
    assert home.is_logged_in(), 'Пользователь не отобразился как залогиненный (не появилась кнопка Выйти).'

@pytest.mark.registration
def test_register_user_invalid_email_mask(driver, base_url):
    home = HomePage(driver)
    auth = AuthModal(driver)

    home.open_home(base_url)
    home.open_auth_modal()
    auth.open_register()

    # Вводим только email, остальное оставляем
    auth.register("", "invalid_email", "")

    # Проверяем ошибки валидации
    auth.expect_invalid_email_error()

@pytest.mark.registration
def test_register_existing_user(driver, base_url):
    # Попытка зарегистрировать уже существующего пользователя по email
    from utils.data import EXISTING_EMAIL
    home = HomePage(driver)
    auth = AuthModal(driver)

    home.open_home(base_url)
    home.open_auth_modal()
    auth.open_register()

    auth.register("User", EXISTING_EMAIL, "AnyPassword1")

    # Ожидаем подсветку ошибок и текст "Ошибка" под email
    auth.expect_invalid_email_error()
