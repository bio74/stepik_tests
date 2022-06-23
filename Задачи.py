
#1.6 2
'''import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
link = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()   
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла'''

#1.6 3
'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
    element.send_keys("Мой ответ")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла'''

#1.6 4

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
link = "http://suninjuly.github.io/find_xpath_form"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
finally:   
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла'''

# Зарегаться на сайте заполнив обязательные поля.

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")  
    input2 = browser.find_element(By.CLASS_NAME, "second")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CLASS_NAME, "third")
    input3.send_keys("test@test.ru")    
    ...
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()'''

#1.6 5

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CLASS_NAME, "first")
    input1.send_keys("Ivan")  
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CLASS_NAME, "third")
    input3.send_keys("test@test.ru")    
    ...
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()'''
    
# 2.1 3

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = x_element.text
    y = calc(x) 
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)  
    input2 = browser.find_element(By.ID, "robotCheckbox").click()
    input3 = browser.find_element(By.ID, 'robotsRule').click()
    button = browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()'''

# 2.1 4

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.TAG_NAME, "img").get_attribute('valuex')
    y = calc(x)
    input2 = browser.find_element(By.ID, "answer").send_keys(y)
    input3 = browser.find_element(By.ID, "robotCheckbox").click()
    input4 = browser.find_element(By.ID, 'robotsRule').click()
    button = browser.find_element(By.TAG_NAME, "button").click() 
finally:
    time.sleep(10)
    browser.quit()'''

# 2.2 1

'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element(By.ID, "num1").text
    x2 = browser.find_element(By.ID, "num2").text
    y = str(int(x1)+int(x2))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)       
    button = browser.find_element(By.TAG_NAME, "button").click() 
finally:
    time.sleep(5)
    browser.quit()'''


# 2.2 2

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    robot = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
    robot.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)    
    button.click()     
finally:
    time.sleep(5)
    browser.quit()'''

# 2.2 3

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("Ivan") 
    browser.find_element(By.NAME, "lastname").send_keys("Ivanov") 
    browser.find_element(By.NAME, "email").send_keys("i@i.ru")    
    current_dir = os.path.abspath(os.path.dirname(__file__))  
    file_path = os.path.join(current_dir, 'file.txt')  
    browser.find_element(By.NAME, "file").send_keys(file_path)
    #print(file_path)
    button = browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(5)
    browser.quit()'''

# 2.3 2

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element(By.CLASS_NAME, "btn").click()
    confirm = browser.switch_to.alert.accept()
    y = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(5)
    browser.quit()'''
    
# 2.3 2

'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element(By.TAG_NAME, "button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    y = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(5)
    browser.quit()'''

# 2.4 2


'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, "book").click()
    y = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()
finally:
    browser.quit()'''

























