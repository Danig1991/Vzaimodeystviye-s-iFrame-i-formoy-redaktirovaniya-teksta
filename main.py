import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# текст для ввода
test_text = "Test text."

# переключение на iFrame
i_frame = driver_chrome.find_element(By.ID, "iFrame1")
driver_chrome.switch_to.frame(i_frame)
print("Переключение на iFrame.")

# очистить содержимое поля, вставить текст и выделить его
input_pole = driver_chrome.find_element(By.XPATH, "//*[@class='rsw-ce']")
input_pole.send_keys(Keys.CONTROL + "a", Keys.DELETE)
print("Поле очищено.")
time.sleep(1)
input_pole.send_keys(test_text, Keys.CONTROL + "a")
print("Ввод текста.")

# отредактировать текст - сделать его жирным, наклонным и подчеркнутым
driver_chrome.find_element(By.XPATH, "//button[@title='Bold']").click()
driver_chrome.find_element(By.XPATH, "//button[@title='Italic']").click()
driver_chrome.find_element(By.XPATH, "//button[@title='Underline']").click()
print("Текст отредактирован - сделан жирным, наклонным и подчеркнутым.")
input_pole.send_keys(Keys.RIGHT)

# проверка, что текст не изменился
value_modified_text = driver_chrome.find_element(
    By.XPATH, "//*[@class='rsw-ce']/b/i/u"
).text
assert test_text == value_modified_text, "Ошибка: Значения должны совпадать."
print("Текст совпадает с изначальным.")

# пауза
time.sleep(2)

# закрыть страницу
driver_chrome.quit()
print("Страница закрыта.")
