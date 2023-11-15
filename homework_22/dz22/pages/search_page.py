from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework_22.dz22.pages.base_page import BasePage


class SearchPageLocators:
    SEARCH_ICON = (By.XPATH, "/html/body/div[1]/div[1]/header/div[2]/div/div[1]/div[2]")
    SEARCH_BOX = (By.NAME, "q")


class SearchPage(BasePage):
    def activate_search(self):
        self.click(SearchPageLocators.SEARCH_ICON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SearchPageLocators.SEARCH_BOX)
        )

    def search(self, text):
        self.enter_text(SearchPageLocators.SEARCH_BOX, text)
        self.press_enter(SearchPageLocators.SEARCH_BOX)
