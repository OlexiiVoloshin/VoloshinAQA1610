from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class LoginPageLocators:
    LOGIN_ICON = (By.XPATH, "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/div[1]")
    EMAIL_FIELD = (By.XPATH, "//*[@id='login']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='pw']")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='form-auth']/div/div/div[4]")
    ACCOUNT_ICON = (By.XPATH, "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/a[1]")
    EMAIL_TEXT = (By.XPATH, "//*[@id='email']")


class LoginPage(BasePage):
    def login(self, username, password):
        self.click(LoginPageLocators.LOGIN_ICON)
        self.enter_text(LoginPageLocators.EMAIL_FIELD, username)
        self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        return self

    def navigate_to_account(self):
        self.click(LoginPageLocators.ACCOUNT_ICON)
        return self

    def get_email_value(self):
        return self.driver.find_element(*LoginPageLocators.EMAIL_TEXT).get_attribute(
            "value"
        )
