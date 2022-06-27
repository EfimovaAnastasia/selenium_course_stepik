# Шаги:
#
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    y = str(math.log(abs(12*math.sin(x))))
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()
    button.click()
    # browser.find_element(By.TAG_NAME, "select").click()
    # browser.find_element(By.CSS_SELECTOR, "[value=answer]").click()
    #select = Select(browser.find_element(By.TAG_NAME, "select"))

    # Отправляем заполненную форму
    #button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    #button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



