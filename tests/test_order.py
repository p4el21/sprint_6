import allure
from pages.Order_page import OrderPage
from src.config import TestData

class TestOrder:
    @allure.title('Проверка успешного оформления заказа с 1ым набором данных')
    @allure.description('Тест проверяет, что можно оформить заказ самоката с первым набором данных')
    def test_order_first_dataset(self, driver):
        order_page = OrderPage(driver)
        order_page.click_to_button_from_up()
        order_page.login(TestData.NAME, TestData.SURNAME, TestData.ADDRESS, TestData.PHONE)
        order_page.wait_for_load_element()
        order_page.order(TestData.DATE, TestData.COMMENT)
        order_page.wait_success_order()
        order_page.check_success_order()

    @allure.title('Проверка успешного оформления заказа со 2ым набором данных')
    @allure.description('Тест проверяет, что можно оформить заказ самоката со вторым набором данных')
    def test_order_second_dataset(self, driver):
        order_page = OrderPage(driver)
        order_page.click_to_button_from_down()
        order_page.login(TestData.NAME1, TestData.SURNAME1, TestData.ADDRESS1, TestData.PHONE1)
        order_page.wait_for_load_element()
        order_page.order(TestData.DATE1, TestData.COMMENT1)
        order_page.wait_success_order()
        order_page.check_success_order()

    @allure.title('Проверка перехода по логотипу "Самоката"')
    @allure.description('Тест проверяет, что при клике на логотип «Самоката» происходит переход на главную страницу «Самоката»')
    def test_logo_samokat(self, driver):
        order_page = OrderPage(driver)
        self.test_order_first_dataset(driver)
        order_page.click_status()
        order_page.check_success_go_to_main()

    @allure.title('Проверка перехода по логотипу "Яндекса"')
    @allure.description('Тест проверяет, что при клике на логотип «Яндекса» происходит переход на главную страницу «Дзена» через редирект')
    def test_logo_yandex(self, driver):
        order_page = OrderPage(driver)
        self.test_order_first_dataset(driver)
        order_page.click_status()
        order_page.check_success_go_to_yandex()

