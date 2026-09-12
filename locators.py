from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""
    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка «Личный кабинет»
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")


class RegistrationPageLocators:
    """Локаторы для страницы регистрации"""
    # Поле «Имя»
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле «Email»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле «Пароль»
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Сообщение об ошибке пароля
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")


class LoginPageLocators:
    """Локаторы для страницы входа"""
    # Поле «Email»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле «Пароль»
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка «Войти»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка «Зарегистрироваться»
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # Ссылка «Восстановить пароль»
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class PersonalCabinetLocators:
    """Локаторы для личного кабинета"""
    # Кнопка «Выйти»
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")


class ConstructorLocators:
    """Локаторы для раздела «Конструктор»"""
    # Раздел «Булки»
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    # Раздел «Соусы»
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    # Раздел «Начинки»
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")