from pages.login_page import LoginPage
from config import Credentials
from pages.main_page import MainPage

"""Модуль с функциями содержащими наиболее используемые сценарии, такие как 
    Авторизация / Переход к необходимой системе. 
    Написаны сокращения дублирования кода """


# TODO Обсудить, может описать переход к подсистеме черз 1 метод с передачей аргумента?


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
