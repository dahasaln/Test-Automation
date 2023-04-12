import pytest
from pages.RegEmail import RegEmail
from pages.auth import *
from pages.settings import *
import time
from selenium.webdriver.common.keys import Keys


"""TRK-030 Проверка восстановления пароля по почте - негативные сценарии.
    В начале теста в поле  Символы требуется одноразовый ручной ввод CAPTCHA. """

@pytest.mark.newpass
@pytest.mark.negative
def test_forgot_password_page(browser):
    # Разделяем email на имя и домен для использования в следующих запросах:
    sign_at = valid_email.find('@')
    mail_name = valid_email[0:sign_at]
    mail_domain = valid_email[sign_at + 1:len(valid_email)]

    page = NewPassPage(browser)
    page.enter_username(valid_email)
    time.sleep(20)  # время на ввод капчи
    page.btn_click_continue()

    time.sleep(30)  # подождём, пока на почту придёт письмо...

    """Проверяем почтовый ящик на наличие писем и достаём ID последнего письма"""
    result_id, status_id = RegEmail().get_id_letter(mail_name, mail_domain)
    # Получаем id письма с кодом из почтового ящика:
    id_letter = result_id[0].get('id')
    # Сверяем полученные данные с нашими ожиданиями
    assert status_id == 200, "status_id error"
    assert id_letter > 0, "id_letter > 0 error"

    """Получаем код регистрации из письма от Ростелекома"""
    result_code, status_code = RegEmail().get_reg_code(mail_name, mail_domain, str(id_letter))

    # Получаем body из текста письма:
    text_body = result_code.get('body')
    # Извлекаем код из текста методом find:
    reg_code = text_body[text_body.find('Ваш код: ') + len('Ваш код: '):
                         text_body.find('Ваш код: ') + len('Ваш код: ') + 6]
    # Сверяем полученные данные с нашими ожиданиями
    assert status_code == 200, "status_code error"
    assert reg_code != '', "reg_code != [] error"

    reg_digit = [int(char) for char in reg_code]
    print(reg_digit)
    browser.implicitly_wait(30)
    for i in range(0, 6):
        browser.find_elements(*NewPassLocators.NEW_PASS_ONETIME_CODE)[i].send_keys(reg_code[i])
        browser.implicitly_wait(5)
    time.sleep(10)
    one_pass = fake_password
    two_pass = valid_pass_reg
    browser.find_element(*NewPassLocators.NEW_PASS_NEW_PASS).send_keys(one_pass)
    time.sleep(3)
    browser.find_element(*NewPassLocators.NEW_PASS_NEW_PASS_CONFIRM).send_keys(two_pass)
    browser.find_element(*NewPassLocators.NEW_PASS_BTN_SAVE).click()
    time.sleep(20)

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == 'Пароли не совпадают'
    print('TRK-030 Пароли не совпадают')
