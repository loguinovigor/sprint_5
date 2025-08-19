from selenium.webdriver.common.by import By

class HomePageLocators:
    LOGIN_REGISTER_BUTTON = (By.CSS_SELECTOR, "button[data-testid='login-register']")
    POST_AD_BUTTON = (By.CSS_SELECTOR, "button[data-testid='post-ad']")

class AuthModalLocators:
    MODAL = (By.CSS_SELECTOR, "div.modal-auth")
    HAVE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='have-account']")
    NO_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='no-account']")

class LoginFormLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

class RegisterFormLocators:
    EMAIL_INPUT = (By.NAME, "email")
    ANY_ERROR_TEXT = (By.CSS_SELECTOR, "p.error")

class HeaderLocators:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='logout']")
