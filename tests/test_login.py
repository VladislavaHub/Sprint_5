from selenium import webdriver
from locators import Locators
from config import BASE_URL

class TestLogin:
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        yield
        self.driver.quit()


    def test_login(self):
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_FIELD).send_keys("user@example.com")
        self.driver.find_element(*Locators.PASSWORD_FIELD).send_keys("password")
        self.driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
        assert self.driver.find_element(*Locators.PERSONAL_CABINET)