from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from math import log, sin


def calc(num):
    return str(log(abs(12*sin(int(num)))))


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser.get(link)
    # дожидаемся, когда цена дома уменьшится до $100 (ожидание выставляем в 12 секунд)
    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '100'))
    # нажимаем кнопку "Book"
    browser.find_element(By.ID, 'book').click()
    # считываем значение для переменной Х и высчитываем функцию от этого значения
    x = browser.find_element(By.ID, 'input_value').text
    answer = calc(x)
    # вводим ответ в текстовое поле
    input_value = browser.find_element(By.ID, 'answer')
    input_value.send_keys(answer)
    # нажимаем кнопку
    browser.find_element(By.ID, 'solve').click()
    # выводим на печать код, полученный в модальном окне Alert
    print(browser.switch_to.alert.text.split(': ')[-1])
    # выводим на экран ошибку, если она возникнет в процессе работы кода
except Exception as ex:
    print(ex)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
