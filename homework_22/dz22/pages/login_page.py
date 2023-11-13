import time
from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class LoginPage(BasePage):
    __LOGIN_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/div[1]",
    )
    __EMAIL_FIELD_XPATH = (By.XPATH, "//*[@id='login']")
    __PASSWORD_FIELD_XPATH = (By.XPATH, "//*[@id='pw']")
    __LOGIN_BUTTON_XPATH = (By.XPATH, "//*[@id='form-auth']/div/div/div[4]")
    __ACCOUNT_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/a[1]",
    )
    __EMAIL_TEXT_XPATH = (By.XPATH, "//*[@id='email']")

    def login(self, username, password):
        self.click(self.__LOGIN_ICON_XPATH)
        time.sleep(3)
        self.enter_text(self.__EMAIL_FIELD_XPATH, username)
        self.enter_text(self.__PASSWORD_FIELD_XPATH, password)
        self.click(self.__LOGIN_BUTTON_XPATH)

    def navigate_to_account(self):
        self.click(self.__ACCOUNT_ICON_XPATH)
        time.sleep(3)

    def get_email_value(self):
        return self.driver.find_element(*self.__EMAIL_TEXT_XPATH).get_attribute("value")
