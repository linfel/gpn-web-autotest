import pytest

from pages.base_page import BasePage
from pages.login_page import LoginPage
from config import Credentials


class TestLoginTest:

    def test_user_should_login(self, browser):
        login_page = LoginPage(browser, Credentials.LOGIN_URL)
        login_page.open()
        login_page.should_login()