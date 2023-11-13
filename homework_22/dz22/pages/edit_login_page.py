import time
from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class EditLoginPage(BasePage):
    __LOGIN_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/div[1]",
    )
    __EMAIL_FIELD_XPATH = (By.XPATH, "//*[@id='login']")
    __PASSWORD_FIELD_XPATH = (By.XPATH, "//*[@id='pw']")
    __LOGIN_BUTTON_XPATH = (By.XPATH, "//*[@id='form-auth']/div/div/div[4]/button")
    __ACCOUNT_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[2]/div/div[3]/a[1]",
    )
    __NAME_FIELD_XPATH = (By.XPATH, "//*[@id='name']")
    __SURNAME_FIELD_XPATH = (By.XPATH, "//*[@id='surname']")
    __SAVE_BUTTON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div/div/div/div/form/div/div[3]/button",
    )
    __POPUP_WINDOW_XPATH = (By.XPATH, "//*[@id='popup__window']")
    __CLOSE_POPUP_XPATH = (By.XPATH, "//*[@id='popup__window']/div[1]")

    def login(self, username, password):
        self.click(self.__LOGIN_ICON_XPATH)
        time.sleep(3)
        self.enter_text(self.__EMAIL_FIELD_XPATH, username)
        self.enter_text(self.__PASSWORD_FIELD_XPATH, password)
        self.click(self.__LOGIN_BUTTON_XPATH)

    def navigate_to_account(self):
        self.click(self.__ACCOUNT_ICON_XPATH)
        time.sleep(3)

    def edit_name_and_surname(self, new_name, new_surname):
        self.enter_text(self.__NAME_FIELD_XPATH, new_name)
        self.enter_text(self.__SURNAME_FIELD_XPATH, new_surname)
        self.click(self.__SAVE_BUTTON_XPATH)
        time.sleep(3)

    def is_popup_visible(self):
        return self.is_visible(self.__POPUP_WINDOW_XPATH)

    def close_popup(self):
        self.click(self.__CLOSE_POPUP_XPATH)
