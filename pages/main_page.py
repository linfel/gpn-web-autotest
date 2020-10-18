from locators import MainPageLocators
from pages.base_page import BasePage
from time import sleep
import allure


class MainPage(BasePage):

    @allure.step("Переход к подсистеме")
    def should_go_to_subsystem(self, subsystem):
        if subsystem == 'crm':
            crm_plate = self.find_crm_plate()
            crm_plate.click()
        elif subsystem == 'marketing':
            marketing_plate = self.find_marketing_plate()
            marketing_plate.click()
        elif subsystem == 'sfa':
            sfa_plate = self.find_sfa_plate()
            sfa_plate.click()
        elif subsystem == 'distributor':
            distributor_panel_plate = self.find_distribution_panel_plate()
            distributor_panel_plate.click()
        elif subsystem == 'mobile':
            mobile_app_palate = self.find_mobile_app_plate()
            mobile_app_palate.click()
        elif subsystem == 'instructions':
            instructions_plate = self.find_instructions_plate()
            instructions_plate.click()
        else:
            raise Exception
        sleep(2)
        assert subsystem in self.browser.current_url, f'There is wrong url: here it is\n{self.browser.current_url}'

    @allure.step("Выход из системы")
    def should_exit_from_system(self):
        exit_button = self.find_exit_button()
        exit_button.click()
        self.wait_until_url_changes()
        assert 'sign-in' in self.browser.current_url, f'There is wrong url: here it is\n{self.browser.current_url}'

    @allure.step("Найти кнопку CRM")
    def find_crm_plate(self):
        self.is_element_present(*MainPageLocators.CRM_PLATE)
        crm_plate = self.browser.find_element(*MainPageLocators.CRM_PLATE)
        return crm_plate

    @allure.step("Найти кнопку Марктинг")
    def find_marketing_plate(self):
        self.is_element_present(*MainPageLocators.MARKETING_PLATE)
        marketing_plate = self.browser.find_element(*MainPageLocators.MARKETING_PLATE)
        return marketing_plate

    @allure.step("Найти кнопку SFA")
    def find_sfa_plate(self):
        self.is_element_present(*MainPageLocators.SFA_PLATE)
        sfa_plate = self.browser.find_element(*MainPageLocators.SFA_PLATE)
        return sfa_plate

    @allure.step("Найти кнопку панель Дистрибьютора ")
    def find_distribution_panel_plate(self):
        self.is_element_present(*MainPageLocators.DISTRIBUTOR_PANEL_PLATE)
        distribution_panel_plate = self.browser.find_element(*MainPageLocators.DISTRIBUTOR_PANEL_PLATE)
        return distribution_panel_plate

    @allure.step("Найти кнопку Мобильное приложение")
    def find_mobile_app_plate(self):
        self.is_element_present(*MainPageLocators.MOBILE_APP_PLATE)
        mobile_app_plate = self.browser.find_element(*MainPageLocators.MOBILE_APP_PLATE)
        return mobile_app_plate

    @allure.step("Найти кнопку Инструкции")
    def find_instructions_plate(self):
        self.is_element_present(*MainPageLocators.INSTRUCTIONS_PLATE)
        instructions_plate = self.browser.find_element(*MainPageLocators.INSTRUCTIONS_PLATE)
        return instructions_plate

    @allure.step("Найти кнопку Выйти")
    def find_exit_button(self):
        self.is_element_present(*MainPageLocators.EXIT_BUTTON)
        exit_button = self.browser.find_element(*MainPageLocators.EXIT_BUTTON)
        return exit_button
