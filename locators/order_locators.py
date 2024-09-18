from selenium.webdriver.common.by import By

class OrderLocators:
    NAME_FIELD = By.XPATH, '//input[@placeholder="* Имя"]'
    SURNAME_FIELD = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS_FIELD = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_FIELD = By.CLASS_NAME, 'select-search__input'
    METRO_STATIONS = By.XPATH, '//*[contains(@class, "Order_Text") and (text()="Сокольники")]'
    PHONE_FIELD = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    ORDER_BUTTON = By.XPATH, '//button[contains(text(), "Далее")]'
    BUTTON = By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[contains(text(), 'Заказать')]"

    INFO_BUTTON = By.XPATH, '//div[contains(text(), "Про аренду")]'
    DATE_FIELD = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    DATE_SELECT = By.XPATH, '//div[contains(@class, "react-datepicker__day--selected")]'
    RENTAL_FIELD = By.CLASS_NAME, 'Dropdown-root'
    RENTAL_COUNT = By.XPATH, '//*[contains(@class, "Dropdown-option") and (text()="сутки")]'
    COLOR_FIELD = By.XPATH, '//*[@id="black"]'
    COMMENT_FIELD = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    BUTTON_ORDER = By.XPATH, './/div[contains(@class, "Order_Buttons")]//button[contains(text(), "Заказать")]'
    FINISH_BUTTON = By.XPATH, '//*[contains(@class, "Button_Butto") and (text()="Да")]'

    WAIT_SUCCESS = By.XPATH, '//button[contains(text(), "Посмотреть статус")]'

    LOGO_SAMOKAT_BUTTON = By.XPATH, "//a[contains(@class, 'Header_LogoScooter') and @href='/']"
    LOGO_YANDEX_BUTTON = By.XPATH, "//a[contains(@class, 'Header_LogoYandex') and @href='//yandex.ru']"

    BUTTON_ORDER_DOWN = By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[contains(text(), 'Заказать')]"