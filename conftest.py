# Фикстура финализатор
# После завершения теста, который вызывал фикстуру,
# выполнение фикстуры продолжится со строки, следующей за строкой со словом yield
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
EXE_PATH = r'..\chromedriver.exe'
options = Options()


# Изменение user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
# Отключим webdriver
options.add_experimental_option("excludeSwitches", ["enable-automation"])#отключение режима webdriver
options.add_experimental_option('useAutomationExtension', False)#отключение режима webdriver
options.add_argument("--disable-extensions")
options.add_argument("--disable-extensions-file-access-check")
options.add_argument("--disable-extensions-http-throttling")
options.add_argument("--disable-infobars")
options.add_argument("--disable-web-security")
# options.add_argument("--disable-blink-features=AutomationControlled") - НЕ РАБОТАЕТ!!!

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test...")
    print("Report:")
    print("-" * 40)
    driver = webdriver.Chrome(chrome_options=options, executable_path=EXE_PATH)
    driver.maximize_window()
    # Проверка параметров на сайте:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)


    yield driver

    driver.quit()
    print("-" * 40)
    print("\nquit browser...")


