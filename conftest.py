from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from pytest import fixture, UsageError
from os import path


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru', help='Choose language: ru, en, fr, de, es, it, ...')


@fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        print('\nstart chrome browser for test...')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        service = ChromeService(ChromeDriverManager().install())
        browser_object = webdriver.Chrome(options=options, service=service)
        browser_object.implicitly_wait(20)  # задаем неявные ожидания в 20 сек., чтобы избежать ложного падения теста
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test...')
        install_dir = '/snap/firefox/current/usr/lib/firefox'
        driver_loc = path.join(install_dir, 'geckodriver')
        binary_loc = path.join(install_dir, 'firefox')
        service = FirefoxService(driver_loc)
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        options.binary_location = binary_loc
        browser_object = webdriver.Firefox(options=options, service=service)
    else:
        raise UsageError('--browser_name should be chrome or firefox')
    yield browser_object
    print('\nquit browser...')
    browser_object.quit()
