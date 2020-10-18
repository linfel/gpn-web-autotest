from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SybSystemLocators
import allure

"""Данный модуль необходим для описания класс базовой вебстраницы
    от которого мы будем наследывать все остальные классы """


class BasePage:
    """Конструктор необходимый для инициализации очередного инстанса страницы
        В него входи объект записанный в переменную broser который из себя представляет инстанс класса определнного
         бразера управляемого специальным драйвером
         Подробнее о том, как формируется инстанс данного класса в модуле conftest.py
         URL указывается всегда
        Так же сразу при инстанцировании нового объекта страницы применяется метод неявного ожидания
        Нужен для стабилизации тестов. Подробнее про неявное ожидание в документации selenium"""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    """Метод для открытия страницы"""

    @allure.step("Открыть страницу")
    def open(self):
        self.browser.get(self.url)

    """Метод позволяющий проверить наличие элемента на странице
        Принимает в качестве аргумента 2 переменные. Как искать и чем
        (в тестах используются кортежи представляющие, из себя метод поиска элемента
        и его селектор"""

    @allure.step("Проверка на присутствие элемента на странице")
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    """Метод повзоляющий проверить ОТСУТСТВИЕ элемента на странице.
        Использовать осмысленно, можно получать ложноположительные тесты"""

    @allure.step("Проверка на отсутствие элемента на странице")
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    """Метод проверяте что элемент был, но в какой-то моент исчес"""

    @allure.step("Проверка на исчезновение элемента на странице, через 4 секунды")
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def wait_until_url_changes(self):
        WebDriverWait(self.browser, timeout=10).until(EC.url_changes(self.browser.current_url))


"""В проекте для большинства сраниц существует смежное поведени для нескольких страниц  
    для них сформирован промежуточный класс, чтобы изолировать их обощенное поведения от базового класса 
    страниц"""


class SubSystems(BasePage):

    """Метод выхода из системы """
    @allure.step("Выход из системы")
    def exit_system(self):
        try:
            self.is_element_present(*SybSystemLocators.EXIT_BUTTON_0)
            locator = SybSystemLocators.EXIT_BUTTON_0
        except NoSuchElementException:
            self.is_element_present(*SybSystemLocators.EXIT_BUTTON_1)
            locator = SybSystemLocators.EXIT_BUTTON_1
        finally:
            exit_button = self.browser.find_element(*locator)
            exit_button.click()

    """Метод для смены системы (Выход на страницу выбора системы)"""

    @allure.step("Смена подсистемы")
    def change_subsystem(self):
        try:
            self.is_element_present(*SybSystemLocators.SUBSYSTEM_CHANGE_BUTTON_0)
            locator = SybSystemLocators.SUBSYSTEM_CHANGE_BUTTON_0
        except NoSuchElementException:
            self.is_element_present(*SybSystemLocators.SUBSYSTEM_CHANGE_BUTTON_1)
            locator = SybSystemLocators.SUBSYSTEM_CHANGE_BUTTON_1
        finally:
            change_subsystem_button = self.browser.find_element(*locator)
            change_subsystem_button.click()

    """Метод для открытия меню по управлению профилем"""

    @allure.step("Открытие меню управления профилем")
    def open_submenu(self):
        self.is_element_present(*SybSystemLocators.SUB_MENU)
        submenu = self.browser.find_element(*SybSystemLocators.SUB_MENU)
        submenu.click()



