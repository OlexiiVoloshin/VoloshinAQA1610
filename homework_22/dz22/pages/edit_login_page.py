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
    def login_and_navigate(self, username, password):
        self.click(EditLoginPageLocators.LOGIN_ICON)
        self.enter_text(EditLoginPageLocators.EMAIL_FIELD, username)
        self.enter_text(EditLoginPageLocators.PASSWORD_FIELD, password)
        self.click(EditLoginPageLocators.LOGIN_BUTTON)
        self.click(EditLoginPageLocators.ACCOUNT_ICON)
        return self

    def edit_name_and_surname(self, new_name, new_surname):
        self.enter_text(EditLoginPageLocators.NAME_FIELD, new_name)
        self.enter_text(EditLoginPageLocators.SURNAME_FIELD, new_surname)
        self.click(EditLoginPageLocators.SAVE_BUTTON)
        return self

    def is_popup_visible_and_close(self):
        popup_visible = self.is_visible(EditLoginPageLocators.POPUP_WINDOW)
        self.click(EditLoginPageLocators.CLOSE_POPUP)
        return popup_visible
