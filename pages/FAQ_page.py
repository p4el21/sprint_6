import allure
from src.config import Config
from locators.FAQ_page_locators import SamokatLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class FAQPage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем загрузки страницы по локатору "Вопросы о важном"')
    def wait_for_load_element(self, wait_locator):
        WebDriverWait(self.driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(wait_locator))

    @allure.step('Ожидаем загрузки ответа по клику на вопрос"')
    def wait_for_click_element(self, wait_locator):
        WebDriverWait(self.driver, Config.TIMEOUT).until(
            EC.element_to_be_clickable(wait_locator))

    @allure.step('Скроллим страницу до блока с вопросами')
    def scroll_to_element(self, scroll_locator):
        questions_section = self.driver.find_element(*scroll_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", questions_section)

    @allure.step('Проверяем, что для определенного вопроса свой ответ')
    def check_question(self, question_locator, answer_locator, expected_text):
        self.scroll_to_element(SamokatLocators.QUESTIONS_SECTION)
        self.wait_for_load_element(SamokatLocators.QUESTIONS_SECTION)
        self.wait_for_click_element(question_locator)
        self.driver.find_element(*question_locator).click()
        answer = self.driver.find_element(*answer_locator)
        assert answer.text == expected_text, f'Ожидается текст: {expected_text}, получен текст: {answer.text}'