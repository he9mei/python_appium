from appium import webdriver
from time import sleep

caps = {}
caps["automationName"] = "UIAutomator2"  #"appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "7.1.1"
caps["deviceName"] = "MJA68TGES4S4SKAY"
caps["browserName"] = "Chrome"
caps["noReset"] = True

driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)

'''
# 使用百度页面有个问题未解决，浏览器设置以及禁止位置，但是每次自动化还是会清除设置，
# 弹出位置信息，影响元素定位导致失败。
driver.get("https://m.baidu.com")
driver.implicitly_wait(10)

search_box=driver.find_element_by_id("index-kw")
search_box.send_keys("appium")
# driver.find_element_by_name("word")
# driver.find_element_by_class_name("se-input adjust-input")

search_bn=driver.find_element_by_id("index-bn")
search_bn.click()
# driver.find_element_by_class_name("se-bn")
'''

driver.get("http://e.dangdang.com/h5/recommend.html?")
driver.implicitly_wait(10)

# 点击查看更多
el_more=driver.find_element_by_class_name("more")
el_more.click()

sleep(5)
driver.quit()

