from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from homework_22.dz22.pages.base_page import BasePage


class SocialLinksPageLocators:
    ABOUT_STORE = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[1]/div/div[2]/ul/li[4]",
    )
    INSTAGRAM_ICON = (By.XPATH, "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[4]")
    FACEBOOK_ICON = (By.XPATH, "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[1]")
    YOUTUBE_ICON = (By.XPATH, "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[2]")


class SocialLinksPage(BasePage):
    def navigate_to_about_store(self):
        self.click(SocialLinksPageLocators.ABOUT_STORE)

    def scroll_to_social_links(self):
        action = ActionChains(self.driver)
        action.move_to_element(
            self.driver.find_element(*SocialLinksPageLocators.FACEBOOK_ICON)
        ).perform()

    def click_instagram_icon(self):
        self.click(SocialLinksPageLocators.INSTAGRAM_ICON)

    def click_facebook_icon(self):
        self.click(SocialLinksPageLocators.FACEBOOK_ICON)

    def click_youtube_icon(self):
        self.click(SocialLinksPageLocators.YOUTUBE_ICON)
