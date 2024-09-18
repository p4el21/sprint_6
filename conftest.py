import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from src.config import Config

def browser_settings():
    firefox_options = webdriver.FirefoxOptions()
    return firefox_options

@pytest.fixture
def driver() -> WebDriver:
    with allure.step("Создаем драйвер"):
        firefox = webdriver.Firefox()
        firefox.maximize_window()
        firefox.get(Config.URL)
    yield firefox
    with allure.step("Закрываем драйвер"):
        firefox.quit()