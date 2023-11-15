import time
from selenium.webdriver.common.by import By
from homework_21.pages.base_page import BasePage


class EditLoginPage(BasePage):
    LOGIN_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/div[1]",
    )
    EMAIL_FIELD_XPATH = (By.XPATH, "//*[@id='login']")
    PASSWORD_FIELD_XPATH = (By.XPATH, "//*[@id='pw']")
    LOGIN_BUTTON_XPATH = (By.XPATH, "//*[@id='form-auth']/div/div/div[4]/button")
    ACCOUNT_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/a[1]",
    )
    NAME_FIELD_XPATH = (By.XPATH, "//*[@id='name']")
    SURNAME_FIELD_XPATH = (By.XPATH, "//*[@id='surname']")
    SAVE_BUTTON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div/div/div/div/form/div/div[3]/button",
    )
    POPUP_WINDOW_XPATH = (By.XPATH, "//*[@id='popup__window']")
    CLOSE_POPUP_XPATH = (By.XPATH, "//*[@id='popup__window']/div[1]")

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

    def edit_name_and_surname(self, new_name, new_surname):
        self.enter_text(self.NAME_FIELD_XPATH, new_name)
        self.enter_text(self.SURNAME_FIELD_XPATH, new_surname)
        self.click(self.SAVE_BUTTON_XPATH)
        time.sleep(3)

    def is_popup_visible(self):
        return self.is_visible(self.POPUP_WINDOW_XPATH)

    def close_popup(self):
        self.click(self.CLOSE_POPUP_XPATH)
