import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_registration_success(self):
        self.driver.find_element(By.XPATH, "//button[text()='Регистрация']").click()
        self.driver.find_element(By.NAME, "name").send_keys("Vlada")
        self.driver.find_element(By.NAME, "email").send_keys("VladaKhrustaleva10333@yandex.ru")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        self.assertTrue(self.driver.find_element(By.XPATH, "//h2[text()='Вы успешно зарегистрировались']"))

    def test_registration_error_incorrect_password(self):
        self.driver.find_element(By.XPATH, "//button[text()='Регистрация']").click()
        self.driver.find_element(By.NAME, "name").send_keys("Vlada")
        self.driver.find_element(By.NAME, "email").send_keys("VladaKhrustaleva10333@yandex.ru")
        self.driver.find_element(By.NAME, "password").send_keys("123")
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        error_message = self.driver.find_element(By.XPATH, "//p[@class='input-error']").text
        self.assertEqual(error_message, "Некорректный пароль")

    def test_login(self):
        self.driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        self._perform_login()

    def _perform_login(self):
        self.driver.find_element(By.NAME, "email").send_keys("VladaKhrustaleva10333@yandex.ru")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        self.assertTrue(self.driver.find_element(By.XPATH, "//h2[text()='Личный кабинет']"))

    def test_transition_to_cabinet(self):
        self.driver.find_element(By.XPATH, "//button[text()='Личный кабинет']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//h2[text()='Личный кабинет']"))

    def test_transition_from_cabinet_to_constructor(self):
        self.driver.find_element(By.XPATH, "//button[text()='Личный кабинет']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Конструктор']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//h2[text()='Соберите бургер']"))

    def test_logout(self):
        self.driver.find_element(By.XPATH, "//button[text()='Личный кабинет']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Выйти']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']"))

    def test_constructor_sections(self):
        self.driver.find_element(By.XPATH, "//button[text()='Конструктор']").click()

        self.driver.find_element(By.XPATH, "//a[text()='Булки']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//h2[text()='Булки']"))

        self.driver.find_element(By.XPATH, "//a[text()='Соусы']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//h2[text()='Соусы']"))

        self.driver.find_element(By.XPATH, "//a[text()='Начинки']").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//h2[text()='Начинки']"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()