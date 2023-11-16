from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from homework_22.dz22.pages.base_page import BasePage


class SocialLinksPageLocators:
    # Локатори для сторінки соціальних посилань
    ABOUT_STORE = (
        By.XPATH,
        "/html/body/div[1]/div[1]/header/div[1]/div/div[2]/ul/li[4]",
    )
    INSTAGRAM_ICON = (By.XPATH, "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[4]")
    FACEBOOK_ICON = (By.XPATH, "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[1]")
    YOUTUBE_ICON = (By.XPATH, "/html/body/div[1]/div[1]/footer/div/form/div/ul/li[2]")


class SocialLinksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SocialLinksPageLocators

    def navigate_to_about_store(self):
        # Навігація до розділу "Про магазин"
        self.click(self.locators.ABOUT_STORE)
        return self

    def scroll_to_social_links(self):
        # Прокрутка сторінки до соціальних посилань
        instagram_icon = self.find_element(self.locators.INSTAGRAM_ICON)
        ActionChains(self.driver).move_to_element(instagram_icon).perform()
        return self

    def click_instagram_icon(self):
        # Клік на іконку Instagram
        self.click(self.locators.INSTAGRAM_ICON)
        return self

    def click_facebook_icon(self):
        # Клік на іконку Facebook
        self.click(self.locators.FACEBOOK_ICON)
        return self

    def click_youtube_icon(self):
        # Клік на іконку YouTube
        self.click(self.locators.YOUTUBE_ICON)
        return self
