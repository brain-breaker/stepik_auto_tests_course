from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from math import log, sin


def calc(num):
    return str(log(abs(12*sin(int(num)))))


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get(link)
    browser.find_element(By.CLASS_NAME, 'btn').click()  # нажимаем кнопку
    # переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # считываем значение для переменной Х и высчитываем функцию от этого значения
    x = browser.find_element(By.ID, 'input_value').text
    answer = calc(x)
    # вводим ответ в текстовое поле
    input_value = browser.find_element(By.ID, 'answer')
    input_value.send_keys(answer)
    # нажимаем кнопку
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    # выводим на печать код, полученный в модальном окне Alert
    print(browser.switch_to.alert.text.split(': ')[-1])
    # выводим на экран ошибку, если она возникнет в процессе работы кода
except Exception as ex:
    print(ex)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
