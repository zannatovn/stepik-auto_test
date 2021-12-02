from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "http://suninjuly.github.io/alert_accept.html"
driver = webdriver.Chrome()
driver.get(url)


try:

    driver.find_element_by_css_selector('.btn-primary').click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    driver.implicitly_wait(5)

    x_value = driver.find_element_by_css_selector('#input_value')
    x = x_value.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    driver.find_element_by_css_selector('#answer').send_keys(y)
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('.btn-primary').click()


except Exception as ex:
    print(ex)

finally:
    time.sleep(3)
    driver.close()
    driver.quit()

