from selenium.webdriver.common.by import By
import time
from homework_21.pages.base_page import BasePage


class HairCategoryPage(BasePage):
    HAIR_CATEGORY_LINK_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[5]/a",
    )
    FILTER_1_XPATH = (By.XPATH, "//*[@id='popularinput-checkbox-2243-40165']")
    FILTER_2_XPATH = (By.XPATH, "//*[@id='input-checkbox-2245-45031']")
    FILTER_3_XPATH = (By.XPATH, "//*[@id='input-checkbox-2257-24219']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_hair_category(self):
        self.click(self.HAIR_CATEGORY_LINK_XPATH)

    def apply_filters(self):
        self.click(self.FILTER_1_XPATH)
        time.sleep(2)
        self.click(self.FILTER_2_XPATH)
        time.sleep(2)
        self.click(self.FILTER_3_XPATH)
        time.sleep(2)
