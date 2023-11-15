from homework_21.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    SEARCH_ICON = (By.XPATH, "/html/body/div[1]/div[1]/header/div[2]/div/div[1]/div[2]")
    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)

    def activate_search(self):
        self.click(self.SEARCH_ICON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )

    def search(self, text):
        self.enter_text(self.SEARCH_BOX, text)
        self.press_enter(self.SEARCH_BOX)
