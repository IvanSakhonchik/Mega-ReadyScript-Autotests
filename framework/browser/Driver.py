from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from framework.utilities.config_manager import config_data


class Driver:
    web_driver = None

    @classmethod
    def get_webdriver(cls):
        if cls.web_driver is None:
            option_browser = config_data["browser_option"]
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(option_browser)
            cls.web_driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        return cls.web_driver

    @classmethod
    def go_to_address(cls, url=config_data["base_url"]):
        cls.web_driver.get(url)

    @classmethod
    def maximize(cls):
        cls.web_driver.maximize_window()

    @classmethod
    def get_url(cls):
        return cls.web_driver.current_url

    @classmethod
    def quit_webdriver(cls):
        if cls.web_driver is not None:
            cls.web_driver.quit()
            cls.web_driver = None
