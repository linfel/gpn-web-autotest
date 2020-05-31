from pages.login_page import LoginPage
from config import Credentials
from pages.main_page import MainPage


def login_scenario(browser):
    login_page = LoginPage(browser, Credentials.LOGIN_URL)
    login_page.open()
    login_page.should_login()


def marketing_scenario(browser):
    login_scenario(browser)
    main_page = MainPage(browser, browser.current_url)
    main_page.should_go_to_subsystem('marketing')


def sfa_scenario(browser):
    login_scenario(browser)
    main_page = MainPage(browser, browser.current_url)
    main_page.should_go_to_subsystem('sfa')


def distributor_panel_scenario(browser):
    login_scenario(browser)
    main_page = MainPage(browser, browser.current_url)
    main_page.should_go_to_subsystem('distributor')


def mobile_app_scenario(browser):
    login_scenario(browser)
    main_page = MainPage(browser, browser.current_url)
    main_page.should_go_to_subsystem('mobile')


def instructions_scenario(browser):
    login_scenario(browser)
    main_page = MainPage(browser, browser.current_url)
    main_page.should_go_to_subsystem('instructions')
