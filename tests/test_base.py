import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Urls:
    BASE = 'https://www.amazon.com'


@pytest.fixture
def driver():
    return webdriver.Chrome(ChromeDriverManager().install())


def test_add_item_to_card(driver):
    driver.get(Urls.BASE)
