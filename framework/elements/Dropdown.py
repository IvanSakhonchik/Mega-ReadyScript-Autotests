from selenium.webdriver.common.by import By

from framework.elements.BaseElement import BaseElement

from framework.browser.Driver import Driver


class Dropdown(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def select_option_by_index(self, index):
        self.click()
        dropdown_item = (Driver.get_webdriver().
                         find_element(By.XPATH, f"//*[@class='dropdown-item rs-in-dialog'][{index}]"))
        dropdown_item.click()
