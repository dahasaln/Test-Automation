import ast
import pickle
import time
import pytest
from pages.auth import *
from pages.settings import *

"""Проверка авторизации по почте и паролю, неверная почта"""
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
           page.check_color(forgot_pass) == '#ff4f12'#Окрашивание надписи "Забыл пароль" в красный цвет
    print('Тест пройден!')
    print(f"\nВаш email: {fake_email} - неверный!")


"""Проверка авторизации по почте и паролю, неверный пароль"""
def test_auth_page_fake_password(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(fake_password)
    time.sleep(20)  # время на ввод CAPTCHA при ее появлении
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           forgot_pass.text == 'Забыл пароль'
    print('Тест пройден!')
    print(f"\nВаш пароль: {fake_password} - неверный!")


""" Проверка авторизации по номеру телефона 'пустой строке' и паролю"""
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


"""Проверка авторизации по номеру телефона и паролю, неверный формат телефона"""
@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('username', [1, 999999999,],
                         ids=['one digit', '9 digits',])
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