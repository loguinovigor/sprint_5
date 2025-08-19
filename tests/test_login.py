import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.data import EXISTING_EMAIL, EXISTING_PASSWORD
from utils.urls import BASE_URL
from locators import HomePageLocators, AuthModalLocators, LoginFormLocators, HeaderLocators

@pytest.mark.login
class TestLogin:
    def test_login_success(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomePageLocators.LOGIN_REGISTER_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthModalLocators.HAVE_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginFormLocators.EMAIL_INPUT)).send_keys(EXISTING_EMAIL)
        driver.find_element(*LoginFormLocators.PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*LoginFormLocators.SUBMIT_BUTTON).click()
        authorized_marker = WebDriverWait(driver, 15).until(EC.presence_of_element_located(HeaderLocators.LOGOUT_BUTTON))
        actual = authorized_marker is not None
        expected = True
        assert actual == expected
