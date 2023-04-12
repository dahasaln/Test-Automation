from selenium.webdriver.common.by import By


class AuthLocators:
    """Локаторы страницы авторизации"""
    AUTH_USERNAME = (By.ID, 'username')#
    AUTH_PASS = (By.ID, 'password')
    AUTH_BTN = (By.ID, 'kc-login')
    AUTH_FORM_ERROR = (By.XPATH, "//span[@id='form-error-message']")#Неверно введен текст с картинки
    AUTH_MESS_ERROR = (By.CSS_SELECTOR, '.rt-input-container__meta--error')#Надпись Введите номер телефона
    AUTH_SPACE_ERROR =(By.XPATH,'//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    AUTH_REG_IN = (By.XPATH, "//a[@id='kc-register']") #Зарегестрироваться
    AUTH_REG_IN_TEMP_CODE = (By.ID, 'back_to_otp_btn')
    AUTH_ACTIVE_TAB_PHON = (By.ID, 't-btn-tab-phone')
    AUTH_ACTIVE_TAB_MAIL = (By.ID, 't-btn-tab-mail')
    AUTH_ACTIVE_TAB_LS = (By.ID,'t-btn-tab-ls')
    AUTH_ACTIVE_TAB_LOGIN = (By.ID,'t-btn-tab-login')
    AUTH_BTN_VK = (By.ID,'oidc_vk')
    AUTH_LOG_VK = (By.XPATH,'//*[@id="oauth_wrap_content"]/div[2]/div/b')
    AUTH_BTN_OK = (By.ID,'oidc_ok')
    AUTH_LOG_OK = (By.XPATH,'//*[@id="widget-el"]/div[1]/div')
    AUTH_BTN_MAIL = (By.ID,'oidc_mail')
    AUTH_LOG_MAIL = (By.XPATH,'//*[@id="wrp"]/div[1]/span')
    AUTH_BTN_GOOGLE = (By.ID,'oidc_google')
    AUTH_LOG_GOOGLE = (By.XPATH,'//*[@id="initialView"]/div[2]/div/div[1]/div/div[2]')
    AUTH_BTN_YA =(By.ID,'oidc_ya')
    AUTH_LOG_YA = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/h1/span')
    AUTH_FORGOT_PASSWORD = (By.ID,'forgot_password')  #Забыл пароль
    AUTH_TERMS_OF_USE = (By.XPATH,'//*[@id="page-right"]/div/div/div/form/div[5]/a')  #Пользовательское соглашение
    AUTH_Public_offer = (By.XPATH,'//*[@id="title"]/h1')
    AUTH_HEADING = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
    AUTH_ACTIVE_TAB = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')







class RegLocators:
    """Локаторы страницы регистрации"""
    REG_FIRSTNAME = (By.XPATH, "//input[@name='firstName']")
    REG_LASTNAME = (By.XPATH, "//input[@name='lastName']")
    REG_REGION = (By.XPATH, "//input[@autocomplete='new-password']"[0])
    REG_ADDRESS = (By.ID, 'address')
    REG_PASSWORD = (By.ID, 'password')
    REG_PASS_CONFIRM = (By.XPATH, "//input[@id='password-confirm']")
    REG_REGISTER = (By.XPATH, "//button[@name='register']")
    REG_CARD_MODAL = (By.XPATH, "//h2[@class='card-modal__title']")


class NewPassLocators:
    """Локаторы страницы восстановления пароля"""
    NEW_PASS_ADDRESS = (By.ID, 'username')
    NEW_PASS_BTN_CONTINUE = (By.ID, 'reset')
    NEW_PASS_ONETIME_CODE = (By.XPATH, '//input[@inputmode="numeric"]')
    NEW_PASS_NEW_PASS = (By.ID, 'password-new')
    NEW_PASS_NEW_PASS_CONFIRM = (By.ID, 'password-confirm')
    NEW_PASS_BTN_SAVE = (By.XPATH, '//button[@id="t-btn-reset-pass"]')

class MainPageLocators():
    PAGE_RIGHT = (By.ID, "page-right") #Страница Авторизация