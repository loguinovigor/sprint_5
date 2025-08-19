from .base_page import BasePage
from locators import HomePageLocators, HeaderLocators, AuthModalLocators

class HomePage(BasePage):
    def open_home(self, base_url):
        self.open(base_url)

    def open_auth_modal(self):
        self.click(HomePageLocators.LOGIN_REGISTER_BUTTON)
        self.visible(AuthModalLocators.MODAL)

    def open_post_ad(self):
        self.click(HomePageLocators.POST_AD_BUTTON)

    def is_logged_in(self):
            # Признак авторизации: в хедере появилась кнопка "Выйти"
            from locators import HeaderLocators
            try:
                self.visible(HeaderLocators.LOGOUT_BUTTON)
                return True
            except Exception:
                return False

    def logout(self):
        self.click(HeaderLocators.LOGOUT_BUTTON)
