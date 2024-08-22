from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.browser.Driver import Driver
from framework.utilities.config_manager import config_data


class BaseElement:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def is_visible(self):
        driver = Driver.get_webdriver()
        wait = WebDriverWait(driver, config_data["wait_element_time"])
        try:
            wait.until(EC.visibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def is_hidden(self):
        driver = Driver.get_webdriver()
        wait = WebDriverWait(driver, config_data["wait_element_time"])
        try:
            wait.until(EC.invisibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def click(self):
        self.get_web_element().click()

    def get_text(self):
        return self.get_web_element().text

    def get_web_element(self):
        return Driver.get_webdriver().find_element(*self.locator)
