import pytest
import allure
import scenarios
from pages.main_page import MainPage
from config import Credentials

"""Моудль с тестами для основной страницы. (Выбор системы)"""


class TestMainPage:

    @allure.step("Тест. Переход к подсистеме")
    @pytest.mark.parametrize('subsystem', Credentials.SUBSYSTEMS)
    def test_go_to_subsystem(self, browser, subsystem):
        scenarios.login_scenario(browser)
        main_page = MainPage(browser, browser.current_url)
        main_page.should_go_to_subsystem(subsystem)

    @allure.step("Тест. Выход.")
    def test_exit_from_system(self, browser):
        scenarios.login_scenario(browser)
        main_page = MainPage(browser, browser.current_url)
        main_page.should_exit_from_system()
