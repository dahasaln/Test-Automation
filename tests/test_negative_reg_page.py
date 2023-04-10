import pytest
from pages.auth import *
from pages.settings import *
import time

#TRK-014 Негативный сценарий регистрации на сайте, невалидный формат Имя,
# в том числе с граничными значениями и XSS инъекциями.
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('firstname', ['', generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(256), english_chars(),
                                       special_chars(), 78489, alternative_keyboard(),japanese_hieroglyph(),
                                       chinese_character(),safety_XSS(),XSS_admixture_HTML()],
                         ids=['14-1) empty line', '14-2) one char', '14-3) 31 chars', '14-4) 256 chars', '14-5) english',
                              '14-6) special', '14-7) number', '14-8) alternative_keyboard', '14-9) japanese_hieroglyph',
                              '14-10) chinese_character','14-11) safety_XSS','14-12) XSS_admixture_HTML'])

def test_get_registration_invalid_format_firstname(browser, firstname):
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(firstname)
    browser.implicitly_wait(2)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(2)
    # Вводим адрес почты/Email:
    page.enter_email(fake_email)
    browser.implicitly_wait(2)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(2)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(2)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')

#TRK-015 Негативный сценарий регистрации на сайте, невалидный формат фамилии,
# в том числе с граничными значениями и XSS инъекциями.
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('lastname', ['', generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(256), english_chars(),
                                       special_chars(), 78489, alternative_keyboard(),japanese_hieroglyph(),
                                       chinese_character(),safety_XSS(),XSS_admixture_HTML()],

                         ids=['15-1) empty line', '15-2) one char', '15-3) 31 chars', '15-4) 256 chars', '15-5) english',
                              '15-6) special', '15-7) number', '15-8) alternative_keyboard', '15-9) japanese_hieroglyph',
                              '15-10) chinese_character','15-11) safety_XSS','15-12) XSS_admixture_HTML'])

def test_get_registration_invalid_format_lastname(browser, lastname):
    """Негативные сценарии регистрации на сайте, невалидный формат фамилии"""

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(fake_email)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')


#TRK-016 Негативный сценарий регистрации на сайте, невалидный формат номера телефона.
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('phone', ['', 7, 7777777777, generate_string_rus(11), english_chars(),special_chars()],
                         ids=['16-1) empty line', '16-2) one digit', '16-3) digits', '16-4) string_rus', '16-5) english_chars',
                              '16-6)special_chars'])
def test_get_registration_invalid_format_phone(browser, phone):
    '''Негативные сценарии регистрации на сайте, невалидный формат номера телефона'''

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(phone)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                              'или email в формате example@email.ru'
    print('Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' 
                              '\nили email в формате example@email.ru')

#TRK-017 Негативный сценарий регистрации на сайте, невалидный формат E-mail.
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('email', ['', '@', '@.', '.', generate_string_rus(20), f'{russian_chars()}@mail.ru',
                                    77777],
                         ids=['17-1) empty line', '17-2) at', '17-3) at point', '17-4) point', '17-5) string', '17-6) russian',
                               '17-7) digits'])
def test_get_registration_invalid_format_email(browser, email):
    """Негативные сценарии регистрации на сайте, невалидный формат почты"""
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(email)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                              'или email в формате example@email.ru'
    print('Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' 
                              '\nили email в формате example@email.ru')

#TRK-018 Проверка, Регистрация в системе: существующий аккаунт по почте
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('address', [ valid_email],
                         ids=['living email'])
def test_get_registration_living_account(browser, address):
    """Негативные сценарии регистрации на сайте, проверка на существование аккаунта по почте"""

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(address)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    card_modal_title = browser.find_element(*RegLocators.REG_CARD_MODAL)

    assert card_modal_title.text == 'Учётная запись уже существует'
    print('TRK-018 Учётная запись уже существует')

#TRK-019 Проверка, Регистрация в системе: поле пароль и подтверждение пароля не совпадают
@pytest.mark.reg
@pytest.mark.negatvie
def test_get_registration_diff_pass_and_pass_conf(browser):
    """Негативные сценарии регистрации на сайте, проверка на совпадение паролей в
    полях ввода 'Пароль' и 'Подтверждение пароля'."""

    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(fake_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(fake_lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(fake_email)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(fake_password)
    browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(valid_pass_reg)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    time.sleep(5)
    assert error_mess.text == 'Пароли не совпадают'
    print('TRK-019 Пароли не совпадают')