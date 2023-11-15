from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class LanguageChangePageLocators:
    MEN_SECTION = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[8]")
    RU_LANGUAGE = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[1]/div/div[3]/ul/li[1]",
    )
    HEADER_TEXT = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/h1")


class LanguageChangePage(BasePage):
    def navigate_to_men_section(self):
        self.click(LanguageChangePageLocators.MEN_SECTION)

    def change_language_to_ru(self):
        self.click(LanguageChangePageLocators.RU_LANGUAGE)

    def get_header_text(self):
        return self.driver.find_element(*LanguageChangePageLocators.HEADER_TEXT).text
