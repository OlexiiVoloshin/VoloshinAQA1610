from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from homework_21.pages.base_page import BasePage


class SocialLinksPage(BasePage):
    ABOUT_STORE_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[1]/div/div[2]/ul/li[4]",
    )
    INSTAGRAM_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[4]",
    )
    FACEBOOK_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[1]",
    )

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_about_store(self):
        self.click(self.ABOUT_STORE_XPATH)

    def scroll_to_social_links(self):
        action = ActionChains(self.driver)
        action.move_to_element(
            self.driver.find_element(*self.FACEBOOK_ICON_XPATH)
        ).perform()

    def click_instagram_icon(self):
        self.click(self.INSTAGRAM_ICON_XPATH)

    def click_facebook_icon(self):
        self.click(self.FACEBOOK_ICON_XPATH)
