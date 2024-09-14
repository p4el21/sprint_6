import allure
from locators.order_locators import OrderLocators
from pages.Order_page import OrderPage
from src.config import TestData
import pytest

class TestOrder:
    @allure.title('Создание объекта order_page класса OrderPage')
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.order_page = OrderPage(driver)

    @allure.title('Проверка успешного оформления заказа с 1ым набором данных')
    @allure.description('Тест проверяет, что можно оформить заказ самоката с первым набором данных')
    def test_order_first_dataset(self):
        self.order_page.click_to_button_from_up()
        self.order_page.login(TestData.NAME, TestData.SURNAME, TestData.ADDRESS, TestData.PHONE)
        self.order_page.wait_for_load_element(OrderLocators.INFO_BUTTON)
        self.order_page.order(TestData.DATE, TestData.COMMENT)
        self.order_page.wait_success_order(OrderLocators.WAIT_SUCCESS)
        self.order_page.check_success_order()

    @allure.title('Проверка успешного оформления заказа со 2ым набором данных')
    @allure.description('Тест проверяет, что можно оформить заказ самоката со вторым набором данных')
    def test_order_second_dataset(self):
        self.order_page.click_to_button_from_down()
        self.order_page.login(TestData.NAME1, TestData.SURNAME1, TestData.ADDRESS1, TestData.PHONE1)
        self.order_page.wait_for_load_element(OrderLocators.INFO_BUTTON)
        self.order_page.order(TestData.DATE1, TestData.COMMENT1)
        self.order_page.wait_success_order(OrderLocators.WAIT_SUCCESS)
        self.order_page.check_success_order()

    @allure.title('Проверка перехода по логотипу "Самоката"')
    @allure.description('Тест проверяет, что при клике на логотип «Самоката» происходит переход на главную страницу «Самоката»')
    def test_logo_samokat(self):
        self.test_order_first_dataset()
        self.order_page.click_status()
        self.order_page.check_success_go_to_main()

    @allure.title('Проверка перехода по логотипу "Яндекса"')
    @allure.description('Тест проверяет, что при клике на логотип «Яндекса» происходит переход на главную страницу «Дзена» через редирект')
    def test_logo_yandex(self):
        self.test_order_first_dataset()
        self.order_page.click_status()
        self.order_page.check_success_go_to_yandex()

