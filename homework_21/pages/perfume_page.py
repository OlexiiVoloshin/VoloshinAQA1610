from selenium.webdriver.common.by import By
from homework_21.pages.base_page import BasePage


class PerfumePage(BasePage):
    PERFUME_BANNER_XPATH = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[3]")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_perfume_page(self):
        self.click(self.PERFUME_BANNER_XPATH)
