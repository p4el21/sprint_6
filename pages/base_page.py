import allure
from selenium.common import TimeoutException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not found within {timeout} seconds.')
            return None

    def click_element(self, locator, timeout = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            print(f'Failed to click on element with {locator}.')

    def get_text(self, locator, timeout = 10):
        element = self.find_element(locator, timeout)
        if element:
            return element.text
        else:
            print(f'Failed to get text on element with {locator}.')
            return None

    def enter_text(self, locator, text, timeout = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Failed to enter text in element with {locator}.')

    def wait_for_element_visible(self, locator, timeout = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not visible after {timeout} seconds.')
            return None

    def wait_for_element_clickable(self, locator, timeout = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f'Element with locator {locator} not clickable after {timeout} seconds.')
            return None

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
