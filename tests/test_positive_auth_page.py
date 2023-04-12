import pytest
import pickle
import time
from pages.locators import AuthLocators
from pages.auth import AuthPage
from pages.settings import valid_email, valid_pass_reg,valid_firstname_reg, valid_lastname_reg

""" TRK-001 Проверка страницы авторизации - дымовое тестирование """
@pytest.mark.reg
@pytest.mark.positive
def test_auth_page_open(browser):
    page = AuthPage(browser)
    print(f"TRK-001 \nCurrently  URL is: {browser.current_url}")
    assert page.get_relative_link() == '/auth/realms/b2c/protocol/openid-connect/auth'

    #Подтверждение отключения user-agent и webdriver
    browser.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(8)

"""TRK-005,TRK-006,TRK-007,TRK-008 Проверка кликабельности табов тел/почта/логин/лицевой счет"""
@pytest.mark.auth
@pytest.mark.positive
def test_switching_tab(browser):
    AuthPage(browser)
    browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_MAIL).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_PHON).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LOGIN).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LS).click()
    time.sleep(2)

    assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_MAIL).text == 'Почта'
    print('\nTRK-005')
    assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_PHON).text == 'Телефон'
    print('TRK-006')
    assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LOGIN).text == 'Логин'
    print('TRK-007')
    assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LS).text == 'Лицевой счёт'
    print('TRK-008')


"""TRK-009-1,TRK-009-2,TRK-009-3,TRK-009-4 Проверка автоматического переключения табов тел/почта/логин/лицевой счет"""
@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.parametrize('username', ['+79167777777', valid_email, 'fake_login', '352010008899'],
                         ids=['TRK-009-1) phone', 'TRK-009-2) E-mail', 'TRK-009-3) login', 'TRK-009-4) ls'])
def test_active_tab(browser, username):

    page  = AuthPage(browser)
    page.enter_username(username)

    page.enter_password(valid_pass_reg)

    if username == '+79167777777':
        time.sleep(2)
        assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB).text == 'Телефон'
        print('TRK-009-1 Телефон')
    elif username == valid_email:
        time.sleep(2)
        assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB).text == 'Почта'
        print('TRK-009-2 Почта')
    elif username == 'fake_login':
        time.sleep(2)
        assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB).text == 'Логин'
        print('TRK-009-3 Логин')
    else:
        time.sleep(2)
        assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB).text == 'Лицевой счёт'
        print('TRK-009-4 Лицевой счёт')


"""TRK-010 Проверка перехода по ссылкам социальных сетей VK"""
def test_jump_to_links_VK(browser):
    AuthPage(browser)
    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators. AUTH_BTN_VK).click()
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_VK)
    print(f"TRK-010 Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_VK).text == 'ВКонтакте'

"""TRK-011 Проверка перехода по ссылкам социальных сетей OK"""
def test_jump_to_links_OK(browser):
    AuthPage(browser)
    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators.AUTH_BTN_OK).click()
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_OK)
    print(f"TRK-011 Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_OK).text == 'Одноклассники'


"""TRK-012 Проверка перехода по ссылкам социальных сетей MAIL"""
def test_jump_to_links_MAIL(browser):
    AuthPage(browser)
    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators.AUTH_BTN_MAIL).click()
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_MAIL)
    print(f"TRK-012 Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_MAIL).text == 'Мой Мир@Mail.Ru'

"""TRK-013 Проверка перехода по ссылкам социальных сетей GOOGLE"""
def test_jump_to_links_(browser):
    AuthPage(browser)
    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators.AUTH_BTN_GOOGLE).click()
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_GOOGLE)
    print(f"TRK-013 Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_GOOGLE).text == 'Войдите в аккаунт Google'

"""TRK-014 Проверка перехода по ссылкам социальных сетей YANDEX """
def test_jump_to_links_YA(browser):
    AuthPage(browser)
    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators.AUTH_BTN_YA).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AUTH_BTN_YA).click()# Лучше кликать 2 раза. dblclick- не помогает.
                    # Вручную, как правило работает с 1ого клика, но не всегда! (в баг не стала вносить!?)
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_YA)
    print(f"TRK-014 Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_YA).text == 'Войдите с Яндекс ID'


"""TRK-023 Проверка Авторизации по почте и паролю. """
def test_auth_page_email_valid(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_pass_reg)
    time.sleep(30)  # время необходимое для ввода Captcha вручную
    page.btn_click_enter()
    page.driver.save_screenshot('TRK_023_auth_by_email.png')
    print('TRK-023 Авторизация прошла успешно!')
    print(
        f"{valid_firstname_reg} {valid_lastname_reg},\nВаш email подтвержден: '{str(valid_email)}'\nВаш пароль подтвержден: '{valid_pass_reg}'\n")
    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(browser.get_cookies(), cookies)

    assert page.get_relative_link() == '/account_b2c/page'












