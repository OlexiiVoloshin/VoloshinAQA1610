from selenium.webdriver.common.by import By
from homework_21.pages.base_page import BasePage


class LanguageChangePage(BasePage):
    MEN_SECTION_XPATH = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[8]")
    RU_LANGUAGE_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[1]/div/div[3]/ul/li[1]",
    )
    HEADER_TEXT_XPATH = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/h1")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_men_section(self):
        self.click(self.MEN_SECTION_XPATH)

    def change_language_to_ru(self):
        self.click(self.RU_LANGUAGE_XPATH)

    def get_header_text(self):
        return self.driver.find_element(*self.HEADER_TEXT_XPATH).text
