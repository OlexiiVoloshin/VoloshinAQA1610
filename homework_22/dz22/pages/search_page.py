from homework_22.dz22.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    __SEARCH_ICON = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[2]/div/div[1]/div[2]",
    )
    __SEARCH_BOX = (By.NAME, "q")

    def activate_search(self):
        self.click(self.__SEARCH_ICON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.__SEARCH_BOX)
        )

    def search(self, text):
        self.enter_text(self.__SEARCH_BOX, text)
        self.press_enter(self.__SEARCH_BOX)
