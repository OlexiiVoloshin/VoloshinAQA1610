from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from homework_22.dz22.pages.base_page import BasePage


class SocialLinksPage(BasePage):
    __ABOUT_STORE_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[1]/div/div[2]/ul/li[4]",
    )
    __INSTAGRAM_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[4]",
    )
    __FACEBOOK_ICON_XPATH = (
        By.XPATH,
        "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[1]",
    )

    def navigate_to_about_store(self):
        self.click(self.__ABOUT_STORE_XPATH)

    def scroll_to_social_links(self):
        action = ActionChains(self.driver)
        action.move_to_element(
            self.driver.find_element(*self.__FACEBOOK_ICON_XPATH)
        ).perform()

    def click_instagram_icon(self):
        self.click(self.__INSTAGRAM_ICON_XPATH)

    def click_facebook_icon(self):
        self.click(self.__FACEBOOK_ICON_XPATH)
