import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(10)

serach_inputbox = driver.find_element_by_id("kw")
serach_inputbox.click()
serach_inputbox.send_keys("selenium")
time.sleep(2)
search_do = driver.find_element_by_id("su")
search_do.click()
time.sleep(5)

driver.quit()

#可以成功调起chrome并完成百度搜索
