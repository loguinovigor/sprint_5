from .base_page import BasePage
from locators import CreateAdLocators

class CreateAdPage(BasePage):
    def fill_form(self, title, description, price, category=None, city=None, condition="new"):
        self.type(CreateAdLocators.TITLE_INPUT, title)
        self.type(CreateAdLocators.DESCRIPTION_TEXTAREA, description)
        self.type(CreateAdLocators.PRICE_INPUT, str(price))

        # Категория
        try:
            cat = self.visible(CreateAdLocators.CATEGORY_DROPDOWN)
            cat.click()
            if category:
                # Выбор элемента выпадающего списка по тексту
                self.click(("xpath", f"//div[contains(@role,'option') or @role='option' or self::li][normalize-space()='{category}'] | //option[normalize-space()='{category}']"))
        except Exception:
            pass

        # Город
        try:
            c = self.visible(CreateAdLocators.CITY_DROPDOWN)
            c.click()
            if city:
                self.click(("xpath", f"//div[contains(@role,'option') or @role='option' or self::li][normalize-space()='{city}'] | //option[normalize-space()='{city}']"))
        except Exception:
            pass

        # Состояние
        if condition == "new":
            try:
                self.click(CreateAdLocators.CONDITION_NEW)
            except Exception:
                pass
        else:
            try:
                self.click(CreateAdLocators.CONDITION_USED)
            except Exception:
                pass

    def publish(self):
        self.click(CreateAdLocators.PUBLISH_BUTTON)
