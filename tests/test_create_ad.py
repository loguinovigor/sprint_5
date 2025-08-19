import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import BASE_URL
from locators import HomePageLocators, AuthModalLocators, LoginFormLocators

@pytest.mark.create_ad
class TestCreateAd:
    def test_anonymous_shows_login_modal(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomePageLocators.POST_AD_BUTTON)).click()
        # assert: модалка авторизации отображается
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthModalLocators.MODAL)),                 "Модалка авторизации не появилась для анонимного пользователя"
        # и видны поля логина
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginFormLocators.EMAIL_INPUT))
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginFormLocators.PASSWORD_INPUT))
