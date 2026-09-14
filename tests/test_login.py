from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from helpers import generate_email, generate_password, generate_name
import pytest


class TestLogin:

    def test_login_from_main_page(self, driver):
        """Вход по кнопке «Войти в аккаунт» на главной"""
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(EC.url_contains("/login"))

    def test_login_from_personal_cabinet(self, driver):
        """Вход через кнопку «Личный кабинет»"""
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON)).click()
        wait.until(EC.url_contains("/login"))

    def test_login_from_registration_form(self, driver):
        """Вход через кнопку в форме регистрации"""
        driver.get("https://stellarburgers.education-services.ru/register")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)).click()
        wait.until(EC.url_contains("/login"))

    def test_login_from_restore_password_form(self, driver):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get("https://stellarburgers.education-services.ru/login")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.RESTORE_PASSWORD_LINK)).click()
        wait.until(EC.url_contains("/forgot-password"))

        # Sprint_5 - финальная версия