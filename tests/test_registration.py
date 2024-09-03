from selenium import webdriver
from locators import Locators
from config import BASE_URL
from tests.data import generate_email

class TestRegistration:

    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        yield
        self.driver.quit()


    def test_registration_success(self):
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
        self.driver.find_element(*Locators.NAME_FIELD).send_keys("Vlada")
        self.driver.find_element(*Locators.EMAIL_FIELD).send_keys(generate_email())
        self.driver.find_element(*Locators.PASSWORD_FIELD).send_keys("123456")
        self.driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
        assert self.driver.find_element(*Locators.SUCCESS_MESSAGE)


    def test_registration_error_incorrect_password(self):
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()
        self.driver.find_element(*Locators.NAME_FIELD).send_keys("Vlada")
        self.driver.find_element(*Locators.EMAIL_FIELD).send_keys(generate_email())
        self.driver.find_element(*Locators.PASSWORD_FIELD).send_keys("123")
        self.driver.find_element(*Locators.REGISTER_SUBMIT_BUTTON).click()
        error_message = self.driver.find_element(*Locators.ERROR_MESSAGE).text
        assert error_message == "Некорректный пароль"
