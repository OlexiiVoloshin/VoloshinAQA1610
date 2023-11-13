from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class LanguageChangePage(BasePage):
    __MEN_SECTION_XPATH = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[8]")
    __RU_LANGUAGE_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[1]/div/div[3]/ul/li[1]",
    )
    __HEADER_TEXT_XPATH = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/h1")

    def navigate_to_men_section(self):
        self.click(self.__MEN_SECTION_XPATH)

    def change_language_to_ru(self):
        self.click(self.__RU_LANGUAGE_XPATH)

    def get_header_text(self):
        return self.driver.find_element(*self.__HEADER_TEXT_XPATH).text
