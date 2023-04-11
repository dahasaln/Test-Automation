import ast
import pickle
import time
import pytest
from pages.auth import *
from pages.settings import *

"""TRK-024 Проверка авторизации по E-mail и паролю,в системе: неверный E-mail"""
def test_auth_page_fake_email(browser):
    page = AuthPage(browser)
    page.enter_username(fake_email)
    page.enter_password(valid_pass_reg)
    time.sleep(30) # время на ввод CAPTCHA при ее появлении
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль'  and \
           forgot_pass.text == 'Забыл пароль' and \
           page.check_color(forgot_pass) == '#ff4f12' # Проверка, что ссылка "Забыл пароль" окрасилась
                                                      # в красный цвет
    print('TRK-024 Тест пройден!')
    print(f"\nВаш email: {fake_email} - неверный!\nCсылка 'Забыл пароль' окрасилась в оранжевый цвет")


"""TRK-025 Проверка авторизации по E-mail и паролю, в системе: неверный пароль"""
def test_auth_page_fake_password(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(fake_password)
    time.sleep(30)  # время на ввод CAPTCHA при ее появлении
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           forgot_pass.text == 'Забыл пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'  # Проверка, что ссылка "Забыл пароль" окрасилась
                                                       # в красный цвет
    print('TRK-025 Тест пройден!')
    print(f"\nВаш пароль: {fake_password} - неверный!\nCсылка 'Забыл пароль' окрасилась в оранжевый цвет")


"""TRK-026 Проверка авторизации по номеру телефона 'пустой строке' и паролю"""
#Дожидаться ввода CAPTCHA не нужно
@pytest.mark.auth
@pytest.mark.negative
def test_auth_page_phone_empty_username(browser):
    page = AuthPage(browser)
    page.enter_username(" ")
    page.btn_click_enter()
    page.enter_password(valid_pass_reg)
    browser.implicitly_wait(10)
    error_mess = browser.find_element(*AuthLocators.AUTH_SPACE_ERROR)
    assert error_mess.text == 'Введите номер телефона'
    print('Тест пройден!')
    print(f"\nВведите номер телефона")


"""TRK-027 Проверка авторизации по номеру телефона и паролю, неверный формат телефона"""
@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('username', [1, 999999999,],
                         ids=['one digit', '9 digits'])
def test_auth_page_invalid_username(browser, username):
    page = AuthPage(browser)
    page.enter_username(username)
    time.sleep(3)
    page.enter_password(valid_pass_reg)
    browser.implicitly_wait(10)
    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Неверный формат телефона'
    print('Тест пройден!')
    print(f"\nНеверный формат телефона")