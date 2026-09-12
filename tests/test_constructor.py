from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators
import pytest


class TestConstructor:

    def test_go_to_buns_section(self, driver):
        """Переход к разделу «Булки»"""
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(ConstructorLocators.BUNS_SECTION)).click()
        # Проверяем, что раздел активен
        assert "Булки" in driver.page_source

    def test_go_to_sauces_section(self, driver):
        """Переход к разделу «Соусы»"""
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_SECTION)).click()
        assert "Соусы" in driver.page_source

    def test_go_to_fillings_section(self, driver):
        """Переход к разделу «Начинки»"""
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(ConstructorLocators.FILLINGS_SECTION)).click()
        assert "Начинки" in driver.page_source
        # Sprint_5 - финальная версия