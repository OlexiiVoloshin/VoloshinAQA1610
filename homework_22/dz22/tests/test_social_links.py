from homework_22.dz22.pages.social_links_page import SocialLinksPage


def test_social_links(
    driver,
    base_url,
    expected_instagram_url,
    expected_facebook_url,
    expected_youtube_url,
):
    driver.get(base_url)
    social_page = SocialLinksPage(driver)
    social_page.navigate_to_about_store()

    main_window_handle = driver.current_window_handle

    # Тестування посилання на Instagram
    social_page.scroll_to_social_links()
    social_page.click_instagram_icon()
    for handle in driver.window_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            assert expected_instagram_url in driver.current_url
            driver.close()
            driver.switch_to.window(main_window_handle)

    # Тестування посилання на Facebook
    social_page.click_facebook_icon()
    for handle in driver.window_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            assert expected_facebook_url in driver.current_url
            driver.close()
            driver.switch_to.window(main_window_handle)

    # Тестування посилання на YouTube
    social_page.click_youtube_icon()
    for handle in driver.window_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            assert expected_youtube_url in driver.current_url
            driver.close()
            driver.switch_to.window(main_window_handle)
