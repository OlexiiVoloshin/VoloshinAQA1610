from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework_22.dz22.pages.base_page import BasePage


class SearchPageLocators:
    # Локатори для сторінки пошуку
    SEARCH_ICON = (By.XPATH, "/html/body/div[1]/div[1]/header/div[2]/div/div[1]/div[2]")
    SEARCH_BOX = (By.NAME, "q")


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SearchPageLocators

    def activate_search(self):
        # Активація поля пошуку
        self.click(self.locators.SEARCH_ICON)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.SEARCH_BOX)
        )
        return self

    def search(self, search_query):
        # Виконання пошукового запиту
        search_box = self.driver.find_element(*self.locators.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(search_query)
        search_box.submit()
        return self
