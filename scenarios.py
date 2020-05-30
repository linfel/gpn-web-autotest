from pages.login_page import LoginPage
from config import Credentials


def login_scenario(browser):
    login_page = LoginPage(browser, Credentials.LOGIN_URL)
    login_page.open()
    login_page.should_login()
