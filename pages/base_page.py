from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def type(self, locator, value, clear=True):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            el.clear()
        el.send_keys(value)
        return el

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def not_visible(self, locator):
        from selenium.common.exceptions import TimeoutException
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
