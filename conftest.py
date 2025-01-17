import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


"""Данный модуль предназначен для хранения и описания фикстур для выполнения тестов 
    Фикстуры инстанцируют обект браузера с заданными параметрами"""

"""Метод позволяющий добавлять кастомные настройки к вызову исполнения тестов
В данный момент можно кастомно указать желаемый браузер для проведения тестов, а так же 
языковая раскладка браузера"""
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru")


"""Основная фикстура на данный момент
Перед выполнением каждого теста инициализирует браузер с указанными параметрами
После завершения теста закрывает браузер
Данная фикстура распространяется на каждую функцию т.е тест
В будущем, при необходимости будет добавлена генерация тестовых данных посредством API сервера"""
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome" and user_language is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options )
    elif browser_name == "firefox" and user_language is not None:
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()