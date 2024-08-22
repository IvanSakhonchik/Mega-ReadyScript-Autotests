import pytest

from framework.browser.Driver import Driver


@pytest.fixture
def browser():
    Driver.get_webdriver()
    Driver.maximize()
    Driver.go_to_address()
    yield
    Driver.quit_webdriver()
