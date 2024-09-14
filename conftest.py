from random import random
import random
import pytest
from selenium import webdriver

from pages.FAQ_page import FAQPage
from src.config import Config

def browser_settings():
    firefox_options = webdriver.FirefoxOptions()
    #chrome_options.add_argument('--headless')
    # width, height = Config.RESOLUTION
    # chrome_options.add_argument(f'--window-size={width}, {height}')
    return firefox_options


@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.maximize_window()
    firefox.get(Config.URL)
    yield firefox
    firefox.quit()

@pytest.fixture
def generate_data():
    data = 'evgeniyandreev10'
    domain = 'yandex.com'
    numbers = random.randint(100, 999)
    email = f'{data}{numbers}@{domain}'
    password = random.randint(100000, 999999)
    return email, password