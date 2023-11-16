from selenium.webdriver.common.by import By
from homework_22.dz22.pages.base_page import BasePage


class PerfumePageLocators:
    PERFUME_BANNER = (By.XPATH, "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[3]")


class PerfumePage(BasePage):
    def navigate_to_perfume(self):
        self.click(PerfumePageLocators.PERFUME_BANNER)
        return self  # повертає поточний об'єкт для подальшого ланцюга викликів
