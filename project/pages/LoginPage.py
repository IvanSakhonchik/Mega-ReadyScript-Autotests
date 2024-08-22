from selenium.webdriver.common.by import By

from framework.elements.Label import Label
from framework.elements.TextField import TextField
from framework.elements.Button import Button
from framework.form.BaseForm import BaseForm


class LoginPage(BaseForm):

    __login_text_field = TextField((By.CSS_SELECTOR, "input[name=login]"), "Login text field")
    __password_text_field = TextField((By.CSS_SELECTOR, "input[name=pass]"), "Password text field")
    __login_button = Button((By.XPATH, "//div[@class='modal-body']//button"), "Login button")
    __invalid_feedback_label = Label((By.CSS_SELECTOR, ".invalid-feedback"), "Invalid feedback label")

    def __init__(self):
        super().__init__((By.CSS_SELECTOR, ".modal-header"), "Main page title")

    def type_login(self, value):
        self.__login_text_field.send_keys(value)

    def type_password(self, value):
        self.__password_text_field.send_keys(value)

    def click_login(self):
        self.__login_button.click()

    def get_invalid_feedback_text(self):
        self.__invalid_feedback_label.is_visible()
        return self.__invalid_feedback_label.get_text()
