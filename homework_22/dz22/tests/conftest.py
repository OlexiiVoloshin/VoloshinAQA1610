import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://makeup.com.ua/ua/"


@pytest.fixture(scope="session")
def expected_instagram_url():
    return "https://www.instagram.com/makeup.ua/"


@pytest.fixture(scope="session")
def expected_facebook_url():
    return "https://www.facebook.com/makeup.ua"


@pytest.fixture(scope="session")
def expected_youtube_url():
    return "https://www.youtube.com/user/makeupcomua"


@pytest.fixture(scope="session")
def login_credentials():
    return {"username": "runyellowjack@gmail.com", "password": "Vtusya23"}


@pytest.fixture(scope="session")
def search_query():
    return "lipstick"


@pytest.fixture(scope="session")
def expected_filtered_url():
    return "https://makeup.com.ua/ua/categorys/255059/#price_from=100&price_to=500"


@pytest.fixture(scope="session")
def expected_perfume_url():
    return "https://makeup.com.ua/ua/categorys/3/"


@pytest.fixture(scope="session")
def expected_url():
    return "https://makeup.com.ua/ua/categorys/20272/#o[2243][]=40165&o[2245][]=45031&o[2257][]=24219"
