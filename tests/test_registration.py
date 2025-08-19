import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import BASE_URL
from utils.generators import random_email
from locators import HomePageLocators, AuthModalLocators, RegisterFormLocators

@pytest.mark.registration
class TestRegistration:
    def test_registration_email_validation_visible(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomePageLocators.LOGIN_REGISTER_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()
        error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegisterFormLocators.ANY_ERROR_TEXT))
        actual = error.is_displayed()
        expected = True
        assert actual == expected

    def test_can_enter_unique_email(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomePageLocators.LOGIN_REGISTER_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()
        unique_email = random_email()
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegisterFormLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(unique_email)
        actual = email_input.get_attribute("value") == unique_email
        expected = True
        assert actual == expected
