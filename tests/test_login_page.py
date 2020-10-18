import allure
from pages.login_page import LoginPage
from config import Credentials


"""Моудль с тестами для страницы авторизации"""


class TestLoginTest:

    @allure.step("Тест1. Авторзицация")
    def test_user_should_login(self, browser):
        login_page = LoginPage(browser, Credentials.LOGIN_URL)
        login_page.open()
        login_page.should_login()