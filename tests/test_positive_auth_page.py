import pickle
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import AuthLocators
from pages.auth import AuthPage

from pages.settings import valid_email, valid_pass_reg,valid_firstname_reg, valid_lastname_reg

def test_active_tab(browser):
    """Проверка автоматического переключения табов тел/почта/логин/лицевой счет"""
    page = AuthPage(browser)
    browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_MAIL).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_PHON).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LOGIN).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LS).click()
    time.sleep(2)

    assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_MAIL).text == 'Почта'
    assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_PHON).text == 'Телефон'
    assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LOGIN).text == 'Логин'
    assert browser.find_element(*AuthLocators.AUTH_ACTIVE_TAB_LS).text == 'Лицевой счёт'

def test_auth_page_email_valid(browser):
    """Проверка авторизации по почте и паролю"""
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_pass_reg)
    time.sleep(30) # на случай появления Captcha, необходимости ее ввода вручную
    page.btn_click_enter()
    page.driver.save_screenshot('auth_by_email.png')
    print('Авторизация прошла успешно!')
    print(f"{valid_firstname_reg} {valid_lastname_reg},\nВаш email подтвержден: '{str(valid_email)}'\nВаш пароль подтвержден: '{valid_pass_reg}'\n")
    with open('my_cookies.txt', 'wb') as cookies:
        pickle.dump(browser.get_cookies(), cookies)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/authenticate'

#Проверка переходов по ссылкам социальных сетей
#VK
def test_jump_to_links_VK(browser):
    page = AuthPage(browser)
    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators. AUTH_BTN_VK).click()
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_VK)
    print(f"Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_VK).text == 'ВКонтакте'
    #OK
def test_jump_to_links_OK(browser):
    page = AuthPage(browser)
    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators.AUTH_BTN_OK).click()
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_OK)
    print(f"Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_OK).text == 'Одноклассники'
def test_jump_to_links_MAIL(browser):
    page = AuthPage(browser)
    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators.AUTH_BTN_MAIL).click()
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_MAIL)
    print(f"Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_MAIL).text == 'Мой Мир@Mail.Ru'
def test_jump_to_links_GOOGLE(browser):
    page = AuthPage(browser)

    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators.AUTH_BTN_GOOGLE).click()
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_GOOGLE)
    print(f"Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_GOOGLE).text == 'Войдите в аккаунт Google'
def test_jump_to_links_YA(browser):#БАГ!!! Нужно кликать 2 раза. dblclick- не помогает.
    page = AuthPage(browser)
    print(f"\nCurrently before transition URL is: {browser.current_url}")
    browser.find_element(*AuthLocators.AUTH_BTN_YA).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AUTH_BTN_YA).click()
    time.sleep(2)
    print(f"\nCurrently after transition URL is: {browser.current_url}")
    logo = browser.find_element(*AuthLocators.AUTH_LOG_YA)
    print(f"Name Logo: {logo.text}")
    time.sleep(2)
    assert browser.find_element(*AuthLocators.AUTH_LOG_YA).text == 'Войдите с Яндекс ID'