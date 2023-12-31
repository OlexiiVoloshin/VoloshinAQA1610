from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from homework_21.pages.base_page import BasePage


class YouTubePage(BasePage):
    YOUTUBE_LINK_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[2]",
    )

    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_youtube_link(self):
        action = ActionChains(self.driver)
        youtube_link = self.driver.find_element(*self.YOUTUBE_LINK_XPATH)
        action.move_to_element(youtube_link).perform()

    def click_youtube_link(self):
        self.click(self.YOUTUBE_LINK_XPATH)
