from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def enter_text(self, by_locator, text):
        self.driver.find_element(*by_locator).send_keys(text)

    def is_visible(self, by_locator):
        return bool(self.driver.find_element(*by_locator))

    def press_enter(self, by_locator):
        self.driver.find_element(*by_locator).send_keys(Keys.ENTER)

    def click_element(self, by, value):
        element = self.driver.find_element(by, value)
        element.click()
