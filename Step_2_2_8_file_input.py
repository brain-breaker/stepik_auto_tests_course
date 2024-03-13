from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from os import path

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)
    # заполняем текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Ivan')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Petrov')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('test@gmail.com')
    # загружаем файл 'file_input.txt' в форму по ссылке
    current_dir = path.abspath(path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = path.join(current_dir, 'file_input.txt')  # добавляем к этому пути имя файла
    # print(current_dir)
    # print(file_path)
    upload_element = browser.find_element(By.ID, 'file')
    upload_element.send_keys(file_path)
    # нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    # выводим на экран ошибку, если она возникнет в процессе работы кода
except Exception as ex:
    print(ex)
finally:
    # успеваем скопировать код за 30 секунд
    sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
