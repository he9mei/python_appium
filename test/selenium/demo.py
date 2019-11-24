import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(10)

driver.quit()

#可以成功调起chrome
