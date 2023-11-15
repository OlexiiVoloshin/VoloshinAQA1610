import time
from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class EditLoginPageLocators:
    LOGIN_ICON = (By.XPATH, "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/div[1]")
    EMAIL_FIELD = (By.XPATH, "//*[@id='login']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='pw']")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='form-auth']/div/div/div[4]/button")
    ACCOUNT_ICON = (By.XPATH, "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/a[1]")
    NAME_FIELD = (By.XPATH, "//*[@id='name']")
    SURNAME_FIELD = (By.XPATH, "//*[@id='surname']")
    SAVE_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div/div/div/div/form/div/div[3]/button",
    )
    POPUP_WINDOW = (By.XPATH, "//*[@id='popup__window']")
    CLOSE_POPUP = (By.XPATH, "//*[@id='popup__window']/div[1]")


class EditLoginPage(BasePage):
    def login(self, username, password):
        self.click(EditLoginPageLocators.LOGIN_ICON)
        time.sleep(3)
        self.enter_text(EditLoginPageLocators.EMAIL_FIELD, username)
        self.enter_text(EditLoginPageLocators.PASSWORD_FIELD, password)
        self.click(EditLoginPageLocators.LOGIN_BUTTON)

    def navigate_to_account(self):
        self.click(EditLoginPageLocators.ACCOUNT_ICON)
        time.sleep(3)

    def edit_name_and_surname(self, new_name, new_surname):
        self.enter_text(EditLoginPageLocators.NAME_FIELD, new_name)
        self.enter_text(EditLoginPageLocators.SURNAME_FIELD, new_surname)
        self.click(EditLoginPageLocators.SAVE_BUTTON)
        time.sleep(3)

    def is_popup_visible(self):
        return self.is_visible(EditLoginPageLocators.POPUP_WINDOW)

    def close_popup(self):
        self.click(EditLoginPageLocators.CLOSE_POPUP)
