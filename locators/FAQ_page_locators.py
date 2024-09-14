from selenium.webdriver.common.by import By

class SamokatLocators:
    QUESTIONS_SECTION = By.XPATH, '//div[text() ="Вопросы о важном"]'
    ANSWER_FIELD = (By.CLASS_NAME, 'Home_FAQ__3uVm4')
    QUESTION_0 = By.ID, 'accordion__heading-0'
    ANSWER_0 = By.ID, 'accordion__panel-0'
    QUESTION_1 = By.ID, 'accordion__heading-1'
    ANSWER_1 = By.ID, 'accordion__panel-1'
    QUESTION_2 = By.ID, 'accordion__heading-2'
    ANSWER_2 = By.ID, 'accordion__panel-2'
    QUESTION_3 = By.ID, 'accordion__heading-3'
    ANSWER_3 = By.ID, 'accordion__panel-3'
    QUESTION_4 = By.ID, 'accordion__heading-4'
    ANSWER_4 = By.ID, 'accordion__panel-4'
    QUESTION_5 = By.ID, 'accordion__heading-5'
    ANSWER_5 = By.ID, 'accordion__panel-5'
    QUESTION_6 = By.ID, 'accordion__heading-6'
    ANSWER_6 = By.ID, 'accordion__panel-6'
    QUESTION_7 = By.ID, 'accordion__heading-7'
    ANSWER_7 = By.ID, 'accordion__panel-7'

    NAME_FIELD = By.XPATH, '//label[contains(text(), "Имя")]/following-sibling::input'
    EMAIL_FIELD = By.XPATH, '//label[contains(text(), "Email")]/following-sibling::input'
    PASSWORD_FIELD = By.XPATH, '//input[@type="password"]'
    REGISTRATION_BUTTON = By.XPATH, '//button[contains(text(), "Зарегистрироваться")]'
    REGISTRATION_LINK = By.LINK_TEXT, 'Зарегистрироваться'
    LOGOUT_BUTTON = By.XPATH, '//button[contains(text(), "Выход")]'
    LOGIN_BUTTON = By.XPATH, '//button[contains(text(), "Войти")]'
    LOGIN_TO_ACCOUNT_BUTTON = By.XPATH, '//*[contains(@class, "button_button")]'
    ORDER_BUTTON = By.XPATH, '//button[contains(text(), "Оформить заказ")]'
    BURGER_TEXT = By.XPATH, '//h1[contains(text(), "Соберите бургер")]'
    ERROR_INPUT = By.CLASS_NAME, "input__error"
    FORGOT_PASSWORD_LINK = By.XPATH, "//a[@href='/forgot-password']"
    LOGIN_LINK = By.XPATH, "//a[@href='/login']"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//a[@href='/account']"
    ACCOUNT_LIST = By.XPATH, '//ul[contains(@class, "Account_list")]'
    COSTRUCTOR_BUTTON = By.XPATH, "//a[contains(@class, 'AppHeader_header') and @href='/']"
    LOGO_BUTTON = By.XPATH, '//a[@href="/"]'
    BUNS_TEXT = By.XPATH, '//span[contains(text(), "Булки")]'
    FILLINGS_TEXT = By.XPATH, '//span[contains(text(), "Начинки")]'
    SAUCES_TEXT = By.XPATH, '//span[contains(text(), "Соусы")]'
    ACTIVE_LINE = By.XPATH, '//span[contains(text(), "Булки")]/parent::div[contains(@class, "tab_tab_type_current")]'
    ACTIVE_LINE1 = By.XPATH, '//span[contains(text(), "Начинки")]/parent::div[contains(@class, "tab_tab_type_current")]'