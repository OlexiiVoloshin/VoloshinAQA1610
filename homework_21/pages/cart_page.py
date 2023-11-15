from selenium.webdriver.common.by import By
import time
from homework_21.pages.base_page import BasePage


class CartPage(BasePage):
    CLOTHING_CATEGORY_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[12]/a",
    )
    MEN_FILTER_XPATH = (By.XPATH, "//*[@id='input-checkbox-2259-22447']")
    SELECT_PRODUCT_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div[5]/ul/li[2]/div[2]/a",
    )
    BUY_BUTTON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div",
    )
    CLOSE_POPUP_XPATH = (By.XPATH, "/html/body/div[1]/div[2]/div/div[2]")
    CART_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/header/div[2]/div/div[3]/div[2]",
    )
    CART_POPUP_XPATH = (By.XPATH, "/html/body/div[1]/div[2]/div")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_clothing_category(self):
        self.click(self.CLOTHING_CATEGORY_XPATH)

    def apply_men_filter(self):
        self.click(self.MEN_FILTER_XPATH)

    def select_product_and_buy(self):
        self.click(self.SELECT_PRODUCT_XPATH)
        time.sleep(3)
        self.click(self.BUY_BUTTON_XPATH)

    def close_popup_and_check_cart(self):
        self.click(self.CLOSE_POPUP_XPATH)
        time.sleep(3)
        self.click(self.CART_ICON_XPATH)
        time.sleep(3)
        return self.is_visible(self.CART_POPUP_XPATH)
