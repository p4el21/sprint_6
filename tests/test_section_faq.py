from locators.FAQ_page_locators import SamokatLocators
from pages.FAQ_page import FAQPage
import pytest
import allure

class TestQuestion:
    @allure.title('Создание объекта faq_page класса FAQPage')
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.faq_page = FAQPage(driver)

    @allure.title('Проверка соответствия ответа на 1ый вопрос')
    @allure.description('Сравниваем ответ на первый вопрос')
    def test_question_0(self):
        expected_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        self.faq_page.check_question(SamokatLocators.QUESTION_0, SamokatLocators.ANSWER_0, expected_text)

    @allure.title('Проверка соответствия ответа на 2ой вопрос')
    @allure.description('Сравниваем ответ на второй вопрос')
    def test_question_1(self):
        expected_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        self.faq_page.check_question(SamokatLocators.QUESTION_1, SamokatLocators.ANSWER_1, expected_text)

    @allure.title('Проверка соответствия ответа на 3ий вопрос')
    @allure.description('Сравниваем ответ на третий вопрос')
    def test_question_2(self):
        expected_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        self.faq_page.check_question(SamokatLocators.QUESTION_2, SamokatLocators.ANSWER_2, expected_text)

    @allure.title('Проверка соответствия ответа на 4ый вопрос')
    @allure.description('Сравниваем ответ на четвертый вопрос')
    def test_question_3(self):
        expected_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        self.faq_page.check_question(SamokatLocators.QUESTION_3, SamokatLocators.ANSWER_3, expected_text)

    @allure.title('Проверка соответствия ответа на 5ый вопрос')
    @allure.description('Сравниваем ответ на пятый вопрос')
    def test_question_4(self):
        expected_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        self.faq_page.check_question(SamokatLocators.QUESTION_4, SamokatLocators.ANSWER_4, expected_text)

    @allure.title('Проверка соответствия ответа на 6ой вопрос')
    @allure.description('Сравниваем ответ на шестой вопрос')
    def test_question_5(self):
        expected_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        self.faq_page.check_question(SamokatLocators.QUESTION_5, SamokatLocators.ANSWER_5, expected_text)

    @allure.title('Проверка соответствия ответа на 7ой вопрос')
    @allure.description('Сравниваем ответ на седьмой вопрос')
    def test_question_6(self):
        expected_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        self.faq_page.check_question(SamokatLocators.QUESTION_6, SamokatLocators.ANSWER_6, expected_text)

    @allure.title('Проверка соответствия ответа на 8ой вопрос')
    @allure.description('Сравниваем ответ на восьмой вопрос')
    def test_question_7(self):
        expected_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        self.faq_page.check_question(SamokatLocators.QUESTION_7, SamokatLocators.ANSWER_7, expected_text)
