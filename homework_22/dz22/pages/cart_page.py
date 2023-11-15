import time
from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class CartPageLocators:
    CLOTHING_CATEGORY = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[12]/a")
    MEN_FILTER = (By.XPATH, "//*[@id='input-checkbox-2259-22447']")
    SELECT_PRODUCT = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div[5]/ul/li[2]/div[2]/a",
    )
    BUY_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div",
    )
    CLOSE_POPUP = (By.XPATH, "/html/body/div[1]/div[2]/div/div[2]")
    CART_ICON = (
        By.XPATH,
        "/html/body/div[1]/div[1]/div[1]/header/div[2]/div/div[3]/div[2]",
    )
    CART_POPUP = (By.XPATH, "/html/body/div[1]/div[2]/div")


class CartPage(BasePage):
    def navigate_to_clothing_category(self):
        self.click(CartPageLocators.CLOTHING_CATEGORY)

    def apply_men_filter(self):
        self.click(CartPageLocators.MEN_FILTER)

    def select_product_and_buy(self):
        self.click(CartPageLocators.SELECT_PRODUCT)
        time.sleep(3)
        self.click(CartPageLocators.BUY_BUTTON)

    def close_popup_and_check_cart(self):
        self.click(CartPageLocators.CLOSE_POPUP)
        time.sleep(3)
        self.click(CartPageLocators.CART_ICON)
        time.sleep(3)
        return self.is_visible(CartPageLocators.CART_POPUP)

    def is_cart_popup_visible(self):
        return self.is_visible(CartPageLocators.CART_POPUP)
