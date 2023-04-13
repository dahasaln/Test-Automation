 <img align="right" alt="GIF" src="https://github.com/arsentieva/arsentieva/blob/main/code.gif?raw=true" width="500" height="320" />

## *28.1. Итоговый проект по автомтизации тестирования* :four_leaf_clover:
## *с использованием* PyTest и Selenium 
#### INTQAP-1034
========================================================================
## Объект тестирования: новый интерфейс авторизации в личном кабинете от заказчика [Ростелеком](https://b2c.passport.rt.ru)
----------------------------------------------------------------------------------
* *Окружение*: Windows 11 Pro Версия:21H2\Google 
* *Браузер*: Chrom 109.0.5414.120, (64 бит)
________________________________________________
### *Для тестирования объекта были использованы*:
### :white_check_mark: автоматизированные и ручные тесты
### :white_check_mark: разбиение на классы эквивалентности
### :white_check_mark: анализ граничных значений
-----------------------------------------------------------
/Чек лист/Тест кейс/Баг репорт можно посмотреть по ссылке: 
## [<img src="https://img.shields.io/badge/Чек лист/Тест кейс/Баг репорт-3914AF?style=for-the-badge&logo=/Чек лист/Тест кейс/Баг репорт&logoColor=ЦВЕТ ЛОГОТИПА"/>](https://docs.google.com/spreadsheets/d/1KOnp581oWDApILyWZXfkm6Y6xhpEp1Gr/edit?usp=sharing&ouid=116953298783582314603&rtpof=true&sd=true):four_leaf_clover:
----------------------------------------------------------

###  В корне проекта содержатся следующие файлы :four_leaf_clover:
Файл conftest.py:
* в данном файле находится фикстура с функцией открытия и закрытия браузера 
* для создания виртуального Пользователя используется код "отключения" webdriver, замена user-agent
#### Файл requirements.txt:
* описаны используемые библиотеки
#### Файл pytest.ini:
* зарегистрированы метки маркировок тестов

--------------------------------------------------------
### В Папке pages :four_leaf_clover:
* RegEmail * GET-запросы к виртуальному почтовому ящику [1secmail.com](https://www.1secmail.com/) для получения валидного 
E-mail и кода для регистрации на странице/восстановления пароля   
* locators * локаторы ID, XPath и CSS на web-элементы сайта   
* auth * функции-обёртки для локаторов, распределённые по классам в зависимости от тематики тестов   
* base * функции для применения к локаторам явных ожиданий, получения главной страницы  и ее текущие пути   
* config * исходные конфигурации   
* settings * учетные данные, используемые в процессе теста
-----------------------------------------------------------
#### :point_up: *Тесты настроены на запуск через Run* 
#### :warning: *Страница `Восстановлнеие пароля`  требует ручной ввод Символов с картинки* 
---------------------------------------------------------
### В Папке tests :four_leaf_clover: 
* test_positive_reg_page  * тестируем позитивные сценарии страницы регистрации   
* test_positive_auth_page  * тестируем позитивные сценарии страницы авторизации 
* test_positive_new_pass_page  * тестируем позитивные сценарии страницы восстановления пароля
* test_negative_reg_page  * тестируем негативные сценарии страницы регистрации 
* test_negative_auth_page  * тестируем негативные сценарии страницы авторизации   
* test_negative_new_pass_page * тестируем негативные сценарии страницы восстановления пароля   
