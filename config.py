"""Модуль содержащий класс с данными, необходимыми для выполнения тестов,"""


class Credentials:
    LOGIN = 'test1'
    PASSWORD = 'test2'
    LOGIN_URL = 'http://websso-dev.gpnsm.gsychev.ru/sign-in'
    # TODO Внести "crm", "mobile", "isnructions" когда данные системы будут работать
    SUBSYSTEMS = ['marketing', 'sfa', 'distributor']
