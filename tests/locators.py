class Locators:
    # Кнопка "Регистрация"
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Регистрация']")

    # Поле "Имя"
    NAME_FIELD = (By.NAME, "name")

    # Поле "Email"
    EMAIL_FIELD = (By.NAME, "email")

    # Поле "Пароль"
    PASSWORD_FIELD = (By.NAME, "password")

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Успешное сообщение о регистрации
    SUCCESS_MESSAGE = (By.XPATH, "//h2[text()='Вы успешно зарегистрировались']")

    # Сообщение об ошибке некорректного пароля
    ERROR_MESSAGE_INCORRECT_PASSWORD = (By.XPATH, "//p[@class='input-error']")

    # Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Кнопка "Войти"
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")

    # Заголовок "Личный кабинет"
    CABINET_HEADER = (By.XPATH, "//h2[text()='Личный кабинет']")

    # Кнопка "Личный кабинет"
    USER_CABINET_BUTTON = (By.XPATH, "//button[text()='Личный кабинет']")

    # Кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

    # Заголовок "Соберите бургер"
    HAMBURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//button[text()='Конструктор']")

    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//a[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//a[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//a[text()='Начинки']")

    # Заголовки секций
    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")
