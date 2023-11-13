import time
from homework_21.pages.youtube_page import YouTubePage


def test_youtube_link(driver):
    base_url = "https://makeup.com.ua/ua/"
    expected_youtube_url = "https://www.youtube.com/user/makeupcomua"

    driver.get(base_url)
    youtube_page = YouTubePage(driver)

    youtube_page.scroll_to_youtube_link()
    youtube_page.click_youtube_link()
    time.sleep(1)

    # Перемикання на нову вкладку
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)  # Чекаємо 5 секунд

    assert (
        expected_youtube_url in driver.current_url
    ), "Посилання YouTube не відкриває очікувану URL-адресу"

    driver.close()  # Закриваємо вкладку YouTube
    driver.switch_to.window(driver.window_handles[0])  # Повертаємося на основну вкладку
