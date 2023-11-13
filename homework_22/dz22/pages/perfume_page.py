from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class PerfumePage(BasePage):
    __PERFUME_BANNER_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[3]",
    )

    def navigate_to_perfume_page(self):
        self.click(self.__PERFUME_BANNER_XPATH)
