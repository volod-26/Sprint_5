import random
import string


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