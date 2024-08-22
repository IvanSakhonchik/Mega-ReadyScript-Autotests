from selenium.webdriver.common.by import By

from framework.elements.Dropdown import Dropdown
from framework.form.BaseForm import BaseForm


class MainPage(BaseForm):

    __personal_account_dropdown = Dropdown((By.CSS_SELECTOR, ".justify-content-end .head-bar__link"), "Next")

    def __init__(self):
        super().__init__((By.CSS_SELECTOR, ".head-logo"), "Main page title")

    def select_option_using_personal_account_dropdown(self, index):
        self.__personal_account_dropdown.select_option_by_index(index)

    def get_text_from_personal_account_dropdown(self):
        return  self.__personal_account_dropdown.get_text()
