from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, PersonalCabinetLocators
from conftest import generate_email, generate_password, generate_name
import pytest


class TestPersonalCabinet:

    def test_go_to_personal_cabinet(self, driver):
        """Переход в личный кабинет"""
        driver.get("https://stellarburgers.education-services.ru/login")
        wait = WebDriverWait(driver, 10)
        
        # Логинимся (нужен существующий аккаунт)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys("test@yandex.ru")
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)).click()
        wait.until(EC.url_contains("/account"))

    def test_logout(self, driver):
        """Выход из аккаунта"""
        driver.get("https://stellarburgers.education-services.ru/login")
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys("test@yandex.ru")
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.LOGOUT_BUTTON)).click()
        wait.until(EC.url_contains("/login"))

    def test_go_to_constructor_from_cabinet(self, driver):
        """Переход из личного кабинета в конструктор"""
        driver.get("https://stellarburgers.education-services.ru/login")
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys("test@yandex.ru")
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("password123")
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.CONSTRUCTOR_BUTTON)).click()
        wait.until(EC.url_contains("/"))