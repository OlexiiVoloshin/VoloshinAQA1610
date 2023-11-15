import time
from homework_22.dz22.pages.perfume_page import PerfumePage


def test_perfume_banner_navigation(driver, base_url, expected_perfume_url):
    driver.get(base_url)
    perfume_page = PerfumePage(driver)
    time.sleep(3)
    perfume_page.navigate_to_perfume_page()

    assert (
        driver.current_url == expected_perfume_url
    ), "URL-адреса не відповідає очікуваній після переходу на сторінку парфумерії"
