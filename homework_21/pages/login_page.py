from selenium.webdriver.common.by import By
import time
from homework_21.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/div[1]",
    )
    EMAIL_FIELD_XPATH = (By.XPATH, "//*[@id='login']")
    PASSWORD_FIELD_XPATH = (By.XPATH, "//*[@id='pw']")
    LOGIN_BUTTON_XPATH = (By.XPATH, "//*[@id='form-auth']/div/div/div[4]")
    ACCOUNT_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/a[1]",
    )
    EMAIL_TEXT_XPATH = (By.XPATH, "//*[@id='email']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.click(self.LOGIN_ICON_XPATH)
        time.sleep(3)
        self.enter_text(self.EMAIL_FIELD_XPATH, username)
        self.enter_text(self.PASSWORD_FIELD_XPATH, password)
        self.click(self.LOGIN_BUTTON_XPATH)

    def navigate_to_account(self):
        self.click(self.ACCOUNT_ICON_XPATH)
        time.sleep(3)

    def get_email_value(self):
        return self.driver.find_element(*self.EMAIL_TEXT_XPATH).get_attribute("value")
