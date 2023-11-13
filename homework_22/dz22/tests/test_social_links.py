import time
from homework_22.dz22.pages.social_links_page import SocialLinksPage


def test_social_links(driver):
    base_url = "https://makeup.com.ua/ua/"
    expected_instagram_url = "https://www.instagram.com/makeup.ua/"
    expected_facebook_url = "https://www.facebook.com/makeup.ua"

    driver.get(base_url)

    social_page = SocialLinksPage(driver)
    social_page.navigate_to_about_store()
    time.sleep(3)

    social_page.scroll_to_social_links()
    social_page.click_instagram_icon()
    time.sleep(3)
    # Перемикання на нову вкладку, якщо вона відкрилась
    driver.switch_to.window(driver.window_handles[-1])
    # Перевірте URL для Instagram
    assert (
        expected_instagram_url in driver.current_url
    ), "Посилання в Instagram не веде на очікувану URL-адресу"

    # Повернутися назад та закрити вкладку
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    social_page.click_facebook_icon()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    # Перевірте URL для Facebook
    assert (
        expected_facebook_url in driver.current_url
    ), "Посилання на Facebook не веде на очікувану URL-адресу"

    # Закрити вкладку та повернутися
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
