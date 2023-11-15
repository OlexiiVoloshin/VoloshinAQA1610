import time
from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class HairCategoryPageLocators:
    HAIR_CATEGORY_LINK = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[5]/a")
    FILTER_1 = (By.XPATH, "//*[@id='popularinput-checkbox-2243-40165']")
    FILTER_2 = (By.XPATH, "//*[@id='input-checkbox-2245-45031']")
    FILTER_3 = (By.XPATH, "//*[@id='input-checkbox-2257-24219']")


class HairCategoryPage(BasePage):
    def navigate_to_hair_category(self):
        self.click(HairCategoryPageLocators.HAIR_CATEGORY_LINK)

    def apply_filters(self):
        self.click(HairCategoryPageLocators.FILTER_1)
        time.sleep(2)
        self.click(HairCategoryPageLocators.FILTER_2)
        time.sleep(2)
        self.click(HairCategoryPageLocators.FILTER_3)
        time.sleep(2)
