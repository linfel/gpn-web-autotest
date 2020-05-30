from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SybSystemLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


class SubSystems(BasePage):

    def exit(self):
        self.is_element_present(*SybSystemLocators.EXIT_BUTTON)
        exit_button = self.browser.find_element(*SybSystemLocators.EXIT_BUTTON)
        exit_button.click()

    def change_subsystem(self):
        self.is_element_present(*SybSystemLocators.SUBSYSTEM_CHANGE_BUTTON)
        change_subsystem_button = self.browser.find_element(*SybSystemLocators.SUBSYSTEM_CHANGE_BUTTON)
        change_subsystem_button.click()

    def open_submenu(self):
        self.is_element_present(*SybSystemLocators.SUB_MENU)
        submenu = self.browser.find_element()
        submenu.click()



