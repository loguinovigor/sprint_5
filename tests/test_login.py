import pytest
from pages.home_page import HomePage
from pages.auth_page import AuthModal
from utils.data import EXISTING_EMAIL, EXISTING_PASSWORD

@pytest.mark.login
def test_login_user_success(driver, base_url):
    home = HomePage(driver)
    auth = AuthModal(driver)

    home.open_home(base_url)
    home.open_auth_modal()
    auth.open_login()
    auth.login(EXISTING_EMAIL, EXISTING_PASSWORD)

    assert home.is_logged_in(), "После логина не отобразился аватар и имя User."
