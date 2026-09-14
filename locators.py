from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")


class RegistrationPageLocators:
    """Локаторы для страницы регистрации"""
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")


class LoginPageLocators:
    """Локаторы для страницы входа"""
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class PersonalCabinetLocators:
    """Локаторы для личного кабинета"""
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")


class ConstructorLocators:
    """Локаторы для раздела «Конструктор»"""
    # Кнопки меню (для клика) — div с классом tab_tab, текст внутри span
    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[text()='Булки']]")
    SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[text()='Соусы']]")
    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[text()='Начинки']]")

    # Заголовки разделов (для проверки) — h2
    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")