import pytest
from pages.auth import *
from pages.settings import *

#Негативный сценарий регистрации на сайте, невалидный формат имени, в том числе с граничными значениями.
@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('firstname', ['', generate_string_rus(1), generate_string_rus(31),
                                       generate_string_rus(777), english_chars(),
                                       special_chars(), 78489],
                         ids=['empty line', 'one char', '31 chars', '777 chars', 'english',
                              'special', 'number'])
def test_get_registration_invalid_format_firstname(browser, firstname):
    """Негативные сценарии регистрации на сайте, невалидный формат имени"""

    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.enter_firstname(firstname)
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
    page.enter_pass_conf(fake_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print('Необходимо заполнить поле кириллицей. От 2 до 30 символов.')


@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('lastname', ['', generate_string_rus(1), generate_string_rus(31),
                                      generate_string_rus(777), english_chars(), special_chars(), 78489],

                         ids=['empty line', 'one char', '31 chars', '256 chars', 'english',
                              'special', 'number'])
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


@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('phone', ['', 1, 7777777777, generate_string_rus(11), special_chars()],
                         ids=['empty line', 'one digit', 'digits', 'string', 'specials'])
def test_get_registration_invalid_format_phone(browser, phone):
    """Негативные сценарии регистрации на сайте, невалидный формат номера телефона"""

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


@pytest.mark.reg
@pytest.mark.negatvie
@pytest.mark.parametrize('email', ['', '@', '@.', '.', generate_string_rus(20), f'{russian_chars()}@mail.ru',
                                    77777],
                         ids=['empty line', 'at', 'at point', 'point', 'string', 'russian',
                               'digits'])
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
    print('Учётная запись уже существует')


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
    assert error_mess.text == 'Пароли не совпадают'
    print('Пароли не совпадают')