from selenium import webdriver
from locators import Locators
from config import BASE_URL

class TestCabinet:

    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        yield
        self.driver.quit()


    def test_transition_to_cabinet(self):
        self.driver.find_element(*Locators.CABINET_BUTTON).click()
        assert self.driver.find_element(*Locators.PERSONAL_CABINET)


    def test_logout(self):
        self.driver.find_element(*Locators.CABINET_BUTTON).click()
        self.driver.find_element(*Locators.LOGOUT_BUTTON).click()
        assert self.driver.find_element(*Locators.BURGER_MESSAGE)

    def test_constructor_sections(self):
        self.driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        self.driver.find_element(*Locators.BUN_TAB).click()
        assert self.driver.find_element(*Locators.BUN_TAB)

        self.driver.find_element(*Locators.SAUCE_TAB).click()
        assert self.driver.find_element(*Locators.SAUCE_TAB)

        self.driver.find_element(*Locators.FILLING_TAB).click()
        assert self.driver.find_element(*Locators.FILLING_TAB)

