import time
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from homework_22.dz22.utils.cookies import Cookies
from homework_22.dz22.utils.local_storage import LocalStorage


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.cookies = Cookies(driver)
        self.local_storage = LocalStorage(driver)

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()
        time.sleep(3)

    def enter_text(self, by_locator, text):
        self.driver.find_element(*by_locator).send_keys(text)
        time.sleep(3)

    def is_visible(self, by_locator):
        return bool(self.driver.find_element(*by_locator))

    def press_enter(self, by_locator):
        self.driver.find_element(*by_locator).send_keys(Keys.ENTER)
        time.sleep(3)

    def click_element(self, by, value):
        element = self.driver.find_element(by, value)
        element.click()
        time.sleep(3)

    def find_element(self, by_locator):
        # Метод для пошуку елемента
        return self.driver.find_element(*by_locator)
