from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators
import pytest


class TestConstructor:

    def test_go_to_buns_section(self, driver):
        """Переход к разделу «Булки»"""
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(ConstructorLocators.BUNS_SECTION))
        driver.execute_script("arguments[0].click();", element)
        header = wait.until(EC.visibility_of_element_located(ConstructorLocators.BUNS_HEADER))
        assert header.text == "Булки"

    def test_go_to_sauces_section(self, driver):
        """Переход к разделу «Соусы»"""
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_SECTION))
        driver.execute_script("arguments[0].click();", element)
        header = wait.until(EC.visibility_of_element_located(ConstructorLocators.SAUCES_HEADER))
        assert header.text == "Соусы"

    def test_go_to_fillings_section(self, driver):
        """Переход к разделу «Начинки»"""
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable(ConstructorLocators.FILLINGS_SECTION))
        driver.execute_script("arguments[0].click();", element)
        header = wait.until(EC.visibility_of_element_located(ConstructorLocators.FILLINGS_HEADER))
        assert header.text == "Начинки"