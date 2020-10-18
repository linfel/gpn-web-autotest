from pages.base_page import BasePage
from locators import LoginPageLocators
from config import Credentials
import allure


class LoginPage(BasePage):

    @allure.step("Авторизация")
    def should_login(self):
        login_input = self.find_login_input()
        login_input.send_keys(Credentials.LOGIN)
        password_input = self.find_password_input()
        password_input.send_keys(Credentials.PASSWORD)
        sign_in_button = self.find_sign_in_button()
        sign_in_button.click()
        self.wait_until_url_changes()
        assert 'subsystems' in self.browser.current_url, f'There is wrong url: here it is\n{self.browser.current_url}'

    @allure.step("Найти поле ввода Логин")
    def find_login_input(self):
        self.is_element_present(*LoginPageLocators.LOGIN_INPUT)
        login_input = self.browser.find_element(*LoginPageLocators.LOGIN_INPUT)
        return login_input

    @allure.step("Найти поле ввода Пароль")
    def find_password_input(self):
        self.is_element_present(*LoginPageLocators.PASSWORD_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        return password_input

    @allure.step("Найти кнопку Войти")
    def find_sign_in_button(self):
        self.is_element_present(*LoginPageLocators.SIGN_IN_BUTTON)
        sign_in_button = self.browser.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
        return sign_in_button
