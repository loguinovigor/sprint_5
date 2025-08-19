from selenium.webdriver.common.by import By

class HomePageLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(.,'Вход') or contains(.,'регистра')]")
    POST_AD_BUTTON = (By.XPATH, "//button[contains(.,'Разместить') and contains(.,'объявл')]")

class AuthModalLocators:
    MODAL = (By.CSS_SELECTOR, "[data-testid='auth-modal']")
    LOGIN_TAB = (By.CSS_SELECTOR, "[data-testid='login-tab']")
    REGISTER_TAB = (By.CSS_SELECTOR, "[data-testid='register-tab']")
    HAVE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-testid='login-tab']")
    NO_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-testid='register-tab']")

class LoginFormLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid='login-password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid='login-submit']")

class RegisterFormLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='register-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid='register-password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid='register-submit']")
    ANY_ERROR_TEXT = (By.CSS_SELECTOR, "[data-testid='email-error']")

class HeaderLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(.,'Выйти')] | //a[contains(.,'Профиль')]")
