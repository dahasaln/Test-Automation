import pickle
import time
import pytest
from selenium.webdriver.common.by import By
from pages.auth import AuthPage
from pages.locators import AuthLocators
from pages.settings import valid_phone, valid_login, valid_password, \
    invalid_ls, valid_email, valid_pass_reg, fake_email, valid_firstname_reg, valid_lastname_reg


# @pytest.mark.auth
# def test_active_tab(browser):
#     """Проверка автоматического переключения табов тел/почта/логин/лицевой счет"""
#
#     browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_PHON)
#     time.sleep(3)
#     browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_MAIL).click()
#     time.sleep(3)
#     browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LOGIN).click()
#     time.sleep(3)
#     browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LS).click()
#
#     # assert browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]').text == 'Мобильный телефон'
#     #
#     # assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_MAIL).text == 'Почта'
#     #
#     # assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LOGIN).text == 'Логин'
#     #
#     # assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LS).text == 'Лицевой счет'





@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.parametrize('username', [valid_phone, valid_login],
                         ids=['valid phone', 'valid login'])
def test_auth_page_phone_login_valid(browser, username):
    """Проверка авторизации по номеру телефона/логину и паролю + проверка
    автоматического переключения табов тел/логин"""
    page = AuthPage(browser)
    page.enter_username(username)
    page.enter_password(valid_password)
    page.btn_click_enter()

    assert page.get_relative_link() == '/account_b2c/page'

@pytest.mark.auth
@pytest.mark.positive
def test_auth_page_email_valid(browser):
    """Проверка авторизации по почте и паролю"""
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_pass_reg)
    time.sleep(25)     # на случай появления Captcha, необходимости ее ввода вручную
    page.btn_click_enter()
    page.driver.save_screenshot('auth_by_email.png')
    print('Авторизация прошла успешно!')
    print(f"{valid_firstname_reg} {valid_lastname_reg},\nВаш email: '{str(valid_email)}'\nВаш пароль: '{valid_pass_reg}'\n")
    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(browser.get_cookies(), cookies)

    assert page.get_relative_link() == '/account_b2c/page'


@pytest.mark.reg
@pytest.mark.positive
def test_reg_page_open(browser):
    """ Проверка страницы регистрации - дымовое тестирование """
    page = AuthPage(browser)
    page.enter_reg_page()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'