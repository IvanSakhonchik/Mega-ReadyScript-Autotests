import pytest
from project.constans.PersonalAccoutOptions import PersonalAccountOptions
from project.pages.MainPage import MainPage
from project.pages.LoginPage import LoginPage
from project.resources.config import LOGIN_EMAIL, LOGIN_PASSWORD
from framework.utilities.config_manager import test_data


@pytest.fixture
def setup_login(browser):
    main_page = MainPage()
    login_page = LoginPage()
    assert main_page.is_page_opened(), "The main page is not opened"
    main_page.select_option_using_personal_account_dropdown(PersonalAccountOptions.Login.value)
    assert login_page.is_page_opened(), "The login page is not opened"
    return login_page, main_page


class TestLogin:

    @pytest.mark.parametrize("email, password", [
        (LOGIN_EMAIL, LOGIN_PASSWORD)
    ])
    def test_successful_login(self, browser, setup_login, email, password):
        login_page, main_page = setup_login
        login_page.type_login(email)
        login_page.type_password(password)
        login_page.click_login()

        assert login_page.is_page_closed(), "The login page is not closed yet"
        actual_personal_account_name = main_page.get_text_from_personal_account_dropdown()
        assert actual_personal_account_name == test_data["personal_account_name"]

    @pytest.mark.parametrize("email, password", [
        ("", ""),
        (test_data["invalid_login"], test_data["invalid_password"]),
        (LOGIN_EMAIL, test_data["invalid_password"]),
        (test_data["invalid_login"], LOGIN_PASSWORD),

    ])
    def test_unsuccessful_login(self, browser, setup_login, email, password):
        login_page, _ = setup_login
        login_page.type_login(email)
        login_page.type_password(password)
        login_page.click_login()

        assert login_page.is_page_opened(), "The login page is not opened"
        actual_invalid_feedback = login_page.get_invalid_feedback_text()
        assert actual_invalid_feedback == test_data["invalid_feedback"]
