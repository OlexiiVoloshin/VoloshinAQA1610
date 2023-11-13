import time
from homework_22.dz22.pages.cart_page import CartPage


def test_add_to_cart(driver):
    base_url = "https://makeup.com.ua/ua/"

    driver.get(base_url)
    cart_page = CartPage(driver)

    cart_page.navigate_to_clothing_category()
    time.sleep(2)
    cart_page.apply_men_filter()
    time.sleep(2)
    cart_page.select_product_and_buy()
    time.sleep(2)
    cart_page.close_popup_and_check_cart()

    assert cart_page.is_cart_popup_visible(), "Спливаюче вікно кошика не з’явилося"
