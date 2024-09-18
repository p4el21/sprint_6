import time
import allure
from locators.order_locators import OrderLocators
from pages.base_page import BasePage
from src.config import Config

class OrderPage(BasePage):

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Нажимаем на кнопку "Заказать" в шапке')
    def click_to_button_from_up(self):
        self.click_element(OrderLocators.BUTTON)

    @allure.step('Вводим данные в поле "Имя"')
    def set_name(self, name):
        self.enter_text(OrderLocators.NAME_FIELD, name)

    @allure.step('Вводим данные в поле "Фамилия"')
    def set_surname(self, surname):
        self.enter_text(OrderLocators.SURNAME_FIELD, surname)

    @allure.step('Вводим данные в поле "Адрес"')
    def set_address(self, address):
        self.enter_text(OrderLocators.ADDRESS_FIELD, address)

    @allure.step('Вводим данные в поле "Метро"')
    def set_metro(self):
        self.click_element(OrderLocators.METRO_FIELD)
        self.click_element(OrderLocators.METRO_STATIONS)

    @allure.step('Вводим данные в поле "Телефон"')
    def set_phone(self, phone):
        self.enter_text(OrderLocators.PHONE_FIELD, phone)

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_sign_in_button(self):
        self.click_element(OrderLocators.ORDER_BUTTON)

    @allure.step('Ожидаем загрузки страницы по локатору "Про аренду"')
    def wait_for_load_element(self):
        self.wait_for_element_visible(OrderLocators.INFO_BUTTON)

    @allure.step('Вводим имя, фамилию, адрес и телефон в соответсвующие поля')
    def login(self, name, surname, address, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro()
        self.set_phone(phone)
        self.click_sign_in_button()

    @allure.step('Вводим данные в поле "Когда привезти самокат"')
    def set_date(self, date):
        self.enter_text(OrderLocators.DATE_FIELD, date)
        self.click_element(OrderLocators.DATE_SELECT)

    @allure.step('Выбираем срок аренды')
    def set_rental(self):
        self.click_element(OrderLocators.RENTAL_FIELD)
        self.click_element(OrderLocators.RENTAL_COUNT)

    @allure.step('Выбираем цвет самоката')
    def set_samokat_color(self):
        self.click_element(OrderLocators.COLOR_FIELD)

    @allure.step('Оставляем комментарий для курьера')
    def set_comment(self, comment):
        self.enter_text(OrderLocators.COMMENT_FIELD, comment)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_to_order(self):
        self.click_element(OrderLocators.BUTTON_ORDER)

    @allure.step('Нажимаем кнопку "Да"')
    def click_to_finish_order(self):
        self.click_element(OrderLocators.FINISH_BUTTON)

    @allure.step('Вводим дату, когда привезти самокат, выбираем срок аренды, цвет самоката и комментарий')
    def order (self, date, comment):
        self.set_date(date)
        self.set_rental()
        self.set_samokat_color()
        self.set_comment(comment)
        self.click_to_order()
        self.click_to_finish_order()

    @allure.step('Смотрим на успешное оформление заказа')
    def check_success_order(self):
        actually_text = self.get_text(OrderLocators.WAIT_SUCCESS)
        expected_text = 'Посмотреть статус'
        assert actually_text == expected_text, f'Ожидается текст: {expected_text}, получен текст: {actually_text}'

    @allure.step('Ожидаем загрузки страницы')
    def wait_success_order(self):
        self.wait_for_element_visible(OrderLocators.WAIT_SUCCESS)

    @allure.step('Нажимаем на кнопку "Посмотреть статус"')
    def click_status(self):
        self.click_element(OrderLocators.WAIT_SUCCESS)

    @allure.step('Нажимаем на логотип самоката')
    def click_logo_samokat(self):
        self.click_element(OrderLocators.LOGO_SAMOKAT_BUTTON)

    @allure.step('Переходим на главную страницу')
    def check_success_go_to_main(self):
        self.click_logo_samokat()
        assert self.driver.current_url == Config.URL

    @allure.step('Нажимаем на логотип Яндекса')
    def click_logo_yandex(self):
        self.click_element(OrderLocators.LOGO_YANDEX_BUTTON)

    @allure.step('Переходим на страницу Дзена')
    def check_success_go_to_yandex(self):
        self.click_logo_yandex()
        self.wait_for_load_page(Config.COUNT_PAGE)
        self.switch_to_page()
        self.wait_url(Config.REDIRECT_URL)
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.step('Нажимаем на кнопку "Заказать" из середины страницы')
    def click_to_button_from_down(self):
        self.click_element(OrderLocators.BUTTON)


