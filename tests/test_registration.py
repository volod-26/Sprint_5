from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators
from conftest import generate_email, generate_password, generate_name
import pytest


class TestRegistration:

    def test_successful_registration(self, driver):
        """Успешная регистрация"""
        driver.get("https://stellarburgers.education-services.ru/register")
        wait = WebDriverWait(driver, 10)
        
        name = generate_name()
        email = generate_email()
        password = generate_password()
        
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # После регистрации должен быть переход на страницу входа
        wait.until(EC.url_contains("/login"))

    def test_registration_with_short_password(self, driver):
        """Ошибка при коротком пароле (меньше 6 символов)"""
        driver.get("https://stellarburgers.education-services.ru/register")
        wait = WebDriverWait(driver, 10)
        
        name = generate_name()
        email = generate_email()
        password = "123"
        
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        error = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR))
        assert error.text == "Некорректный пароль"