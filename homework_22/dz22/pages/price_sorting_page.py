import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from homework_22.dz22.pages.base_page import BasePage


class PriceSortingPageLocators:
    CATEGORY = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[9]")
    SUBCATEGORY = (
        By.XPATH,
        "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[9]/div/div[1]/div[3]/div[1]/div/a",
    )
    PRICE_FILTER = (By.XPATH, "//*[@id='filter-block-wrap']/div[12]")
    PRICE_FROM = (By.XPATH, "//*[@id='price-from']")
    PRICE_TO = (By.XPATH, "//*[@id='price-to']")


class PriceSortingPage(BasePage):
    def navigate_to_category_and_select(self):
        category = self.driver.find_element(*PriceSortingPageLocators.CATEGORY)
        subcategory = self.driver.find_element(*PriceSortingPageLocators.SUBCATEGORY)

        actions = ActionChains(self.driver)
        actions.move_to_element(category).perform()
        time.sleep(3)
        subcategory.click()

    def apply_price_filter(self, price_from, price_to):
        self.click(PriceSortingPageLocators.PRICE_FILTER)
        time.sleep(3)
        price_from_field = self.driver.find_element(
            *PriceSortingPageLocators.PRICE_FROM
        )
        price_to_field = self.driver.find_element(*PriceSortingPageLocators.PRICE_TO)

        price_from_field.clear()
        price_from_field.send_keys(str(price_from))
        price_to_field.clear()
        price_to_field.send_keys(str(price_to))
        price_to_field.send_keys(Keys.ENTER)
