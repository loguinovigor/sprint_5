from .base_page import BasePage
from locators import AuthModalLocators, RegisterFormLocators, LoginFormLocators, HomePageLocators

class AuthModal(BasePage):
    def open_register(self):
        self.click(AuthModalLocators.NO_ACCOUNT_BUTTON)
        self.visible(RegisterFormLocators.FORM)

    def register(self, name, email, password):
        self.type(RegisterFormLocators.NAME_INPUT, name)
        self.type(RegisterFormLocators.EMAIL_INPUT, email)
        self.type(RegisterFormLocators.PASSWORD_INPUT, password)
        self.type(RegisterFormLocators.PASSWORD_REPEAT_INPUT, password)
        self.click(RegisterFormLocators.CREATE_ACCOUNT_BUTTON)

    def open_login(self):
        # На случай если сразу открылась форма логина — просто удостоверимся
        try:
            self.visible(LoginFormLocators.FORM)
        except Exception:
            # переключиться
            self.click(AuthModalLocators.HAVE_ACCOUNT_BUTTON)
            self.visible(LoginFormLocators.FORM)

    def login(self, email, password):
        self.type(LoginFormLocators.EMAIL_INPUT, email)
        self.type(LoginFormLocators.PASSWORD_INPUT, password)
        self.click(LoginFormLocators.SUBMIT_BUTTON)

    def expect_invalid_email_error(self):
            from locators import RegisterFormLocators
            self.visible(RegisterFormLocators.ANY_ERROR_TEXT)