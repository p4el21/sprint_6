import allure
from pages.base_page import BasePage
from locators.faq_page_locators import SamokatLocators

class FAQPage(BasePage):
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ожидаем загрузки страницы по локатору "Вопросы о важном"')
    def wait_for_load_element(self):
        self.wait_for_element_visible(SamokatLocators.QUESTIONS_SECTION)

    @allure.step('Ожидаем загрузки ответа по клику на вопрос"')
    def wait_for_click_element(self, question_locator):
        self.wait_for_element_clickable(question_locator)

    @allure.step('Скроллим страницу до блока с вопросами')
    def scroll_element(self):
        self.scroll_to_element(SamokatLocators.QUESTIONS_SECTION)

    @allure.step('Проверяем, что для определенного вопроса свой ответ')
    def check_question(self, question_locator, answer_locator, expected_text):
        self.scroll_element()
        self.wait_for_load_element()
        self.wait_for_click_element(question_locator)
        self.click_element(question_locator)
        answer = self.find_element(answer_locator)
        assert answer.text == expected_text, f'Ожидается текст: {expected_text}, получен текст: {answer.text}'