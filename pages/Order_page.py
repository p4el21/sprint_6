import time
import allure
from locators.order_locators import OrderLocators
from src.config import Config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на кнопку "Заказать" в шапке')
    def click_to_button_from_up(self):
        self.driver.find_element(*OrderLocators.BUTTON).click()

    @allure.step('Вводим данные в поле "Имя"')
    def set_name(self, name):
        self.driver.find_element(*OrderLocators.NAME_FIELD).send_keys(name)

    @allure.step('Вводим данные в поле "Фамилия"')
    def set_surname(self, surname):
        self.driver.find_element(*OrderLocators.SURNAME_FIELD).send_keys(surname)

    @allure.step('Вводим данные в поле "Адрес"')
    def set_address(self, address):
        self.driver.find_element(*OrderLocators.ADDRESS_FIELD).send_keys(address)

    @allure.step('Вводим данные в поле "Метро"')
    def set_metro(self):
        self.driver.find_element(*OrderLocators.METRO_FIELD).click()
        self.driver.find_element(*OrderLocators.METRO_STATIONS).click()

    @allure.step('Вводим данные в поле "Телефон"')
    def set_phone(self, phone):
        self.driver.find_element(*OrderLocators.PHONE_FIELD).send_keys(phone)

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_sign_in_button(self):
        self.driver.find_element(*OrderLocators.ORDER_BUTTON).click()

    @allure.step('Ожидаем загрузки страницы по локатору "Про аренду"')
    def wait_for_load_element(self, wait_locator):
        WebDriverWait(self.driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(wait_locator))

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
        self.driver.find_element(*OrderLocators.DATE_FIELD).send_keys(date)
        self.driver.find_element(*OrderLocators.DATE_SELECT).click()

    @allure.step('Выбираем срок аренды')
    def set_rental(self):
        self.driver.find_element(*OrderLocators.RENTAL_FIELD).click()
        self.driver.find_element(*OrderLocators.RENTAL_COUNT).click()

    @allure.step('Выбираем цвет самоката')
    def set_samokat_color(self):
        self.driver.find_element(*OrderLocators.COLOR_FIELD).click()

    @allure.step('Оставляем комментарий для курьера')
    def set_comment(self, comment):
        self.driver.find_element(*OrderLocators.COMMENT_FIELD).send_keys(comment)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_to_order(self):
        self.driver.find_element(*OrderLocators.BUTTON_ORDER).click()

    @allure.step('Нажимаем кнопку "Да"')
    def click_to_finish_order(self):
        self.driver.find_element(*OrderLocators.FINISH_BUTTON).click()

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
        actually_text = self.driver.find_element(*OrderLocators.WAIT_SUCCESS).text
        expected_text = 'Посмотреть статус'
        assert actually_text == expected_text, f'Ожидается текст: {expected_text}, получен текст: {actually_text}'

    @allure.step('Ожидаем загрузки страницы')
    def wait_success_order(self, wait_success_locator):
        WebDriverWait(self.driver, Config.TIMEOUT).until(
            EC.visibility_of_element_located(wait_success_locator))

    @allure.step('Нажимаем на кнопку "Посмотреть статус"')
    def click_status(self):
        self.driver.find_element(*OrderLocators.WAIT_SUCCESS).click()

    @allure.step('Нажимаем на логотип самоката')
    def click_logo_samokat(self):
        self.driver.find_element(*OrderLocators.LOGO_SAMOKAT_BUTTON).click()

    @allure.step('Перреходим на главную страницу')
    def check_success_go_to_main(self):
        self.click_logo_samokat()
        assert self.driver.current_url == Config.URL

    @allure.step('Нажимаем на логотип Яндекса')
    def click_logo_yandex(self):
        self.driver.find_element(*OrderLocators.LOGO_YANDEX_BUTTON).click()

    @allure.step('Переходим на страницу Дзена')
    def check_success_go_to_yandex(self):
        self.click_logo_yandex()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.step('Нажимаем на кнопку "Заказать" из середины страницы')
    def click_to_button_from_down(self):
        self.driver.find_element(*OrderLocators.BUTTON).click()


