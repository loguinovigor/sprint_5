from .base_page import BasePage
from locators import ProfilePageLocators

class ProfilePage(BasePage):
    def assert_ad_visible(self, title):
        self.visible(ProfilePageLocators.MY_ADS_BLOCK)
        self.visible(ProfilePageLocators.MY_AD_CARD_BY_TITLE(title))
