from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_INPUT = (By.CSS_SELECTOR, '[placeholder="Логин"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[placeholder="Пароль"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.w-100.sign-in__form-submit')


class MainPageLocators:
    CRM_PLATE = (By.CSS_SELECTOR, '.subsystem-card__image--CRM')
    MARKETING_PLATE = (By.CSS_SELECTOR, '.subsystem-card__image--Marketing')
    SFA_PLATE = (By.CSS_SELECTOR, '.subsystem-card__image--SFA')
    DISTRIBUTOR_PANEL_PLATE = (By.CSS_SELECTOR, '.subsystem-card__image--Distributor')
    MOBILE_APP_PLATE = (By.CSS_SELECTOR, '.subsystem-card__image--MobileApp')
    INSTRUCTIONS_PLATE = (By.CSS_SELECTOR, '.subsystem-card__image--Guide')
    EXIT_BUTTON = (By.CSS_SELECTOR, 'div.sidenav__exit-button')


class SybSystemLocators:
    SUB_MENU = (By.CSS_SELECTOR, '')
    SUBSYSTEM_CHANGE_BUTTON = (By.CSS_SELECTOR, '')
    EXIT_BUTTON = (By.CSS_SELECTOR, '')
