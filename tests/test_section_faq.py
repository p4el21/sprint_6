from locators.faq_page_locators import SamokatLocators
from pages.FAQ_page import FAQPage
import pytest
import allure
from src.data import FAQAnswers

class TestQuestion:
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text',[
        (SamokatLocators.QUESTION_0, SamokatLocators.ANSWER_0, FAQAnswers.ANSWER0),
        (SamokatLocators.QUESTION_1, SamokatLocators.ANSWER_1, FAQAnswers.ANSWER1),
        (SamokatLocators.QUESTION_2, SamokatLocators.ANSWER_2, FAQAnswers.ANSWER2),
        (SamokatLocators.QUESTION_3, SamokatLocators.ANSWER_3, FAQAnswers.ANSWER3),
        (SamokatLocators.QUESTION_4, SamokatLocators.ANSWER_4, FAQAnswers.ANSWER4),
        (SamokatLocators.QUESTION_5, SamokatLocators.ANSWER_5, FAQAnswers.ANSWER5),
        (SamokatLocators.QUESTION_6, SamokatLocators.ANSWER_6, FAQAnswers.ANSWER6),
        (SamokatLocators.QUESTION_7, SamokatLocators.ANSWER_7, FAQAnswers.ANSWER7)])

    @allure.title('Проверка соответствия ответа на вопрос')
    @allure.description('Сравниваем ответ на вопрос')
    def test_questions(self, driver, question_locator, answer_locator, expected_text):
        faq_page = FAQPage(driver)
        faq_page.check_question(question_locator, answer_locator, expected_text)


