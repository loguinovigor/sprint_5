import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import BASE_URL
from locators import HomePageLocators, AuthModalLocators, RegisterFormLocators

@pytest.mark.registration
class TestRegistration:
    def test_registration_email_validation(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomePageLocators.LOGIN_REGISTER_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AuthModalLocators.NO_ACCOUNT_BUTTON)).click()
        # assert: отображается ошибка валидации email
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegisterFormLocators.ANY_ERROR_TEXT)),                 "Ожидалась ошибка валидации email на форме регистрации"
