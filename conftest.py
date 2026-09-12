import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """Фикстура для запуска и закрытия браузера"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def generate_email():
    """Генератор email"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{random_string}@yandex.ru"


def generate_password():
    """Генератор пароля (минимум 6 символов)"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


def generate_name():
    """Генератор имени"""
    return ''.join(random.choices(string.ascii_letters, k=6))