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
    SUB_MENU = (By.CSS_SELECTOR, 'app-profile-block > div > button.mat-icon-button')
    SUBSYSTEM_CHANGE_BUTTON_0 = (By.CSS_SELECTOR, '#cdk-overlay-0 > div > div > div > div :nth-child(2)')
    SUBSYSTEM_CHANGE_BUTTON_1 = (By.CSS_SELECTOR, '#cdk-overlay-1 > div > div > div > div :nth-child(2)')
    EXIT_BUTTON_0 = (By.CSS_SELECTOR, '#cdk-overlay-0 > div > div > div > div :nth-child(4)')
    EXIT_BUTTON_1 = (By.CSS_SELECTOR, '#cdk-overlay-1 > div > div > div > div :nth-child(4)')
