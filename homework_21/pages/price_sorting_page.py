from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from homework_21.pages.base_page import BasePage


class PriceSortingPage(BasePage):
    CATEGORY_XPATH = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[9]")
    SUBCATEGORY_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[9]/div/div[1]/div[3]/div[1]/div/a",
    )
    PRICE_FILTER_XPATH = (By.XPATH, "//*[@id='filter-block-wrap']/div[12]")
    PRICE_FROM_XPATH = (By.XPATH, "//*[@id='price-from']")
    PRICE_TO_XPATH = (By.XPATH, "//*[@id='price-to']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_category_and_select(self):
        category = self.driver.find_element(*self.CATEGORY_XPATH)
        subcategory = self.driver.find_element(*self.SUBCATEGORY_XPATH)

        actions = ActionChains(self.driver)
        actions.move_to_element(category).perform()
        time.sleep(3)
        subcategory.click()

    def apply_price_filter(self, price_from, price_to):
        self.click(self.PRICE_FILTER_XPATH)
        time.sleep(3)
        price_from_field = self.driver.find_element(*self.PRICE_FROM_XPATH)
        price_to_field = self.driver.find_element(*self.PRICE_TO_XPATH)

        price_from_field.clear()
        price_from_field.send_keys(str(price_from))
        price_to_field.clear()
        price_to_field.send_keys(str(price_to))
        price_to_field.send_keys(Keys.ENTER)
