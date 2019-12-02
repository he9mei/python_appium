# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver

caps = {}
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0.1"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "com.tencent.mobileqq"
caps["appActivity"] = ".activity.SplashActivity"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#隐式等待
driver.implicitly_wait(10)

el1 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el1.clear()
el1.send_keys("1062304071")
el2 = driver.find_element_by_accessibility_id("密码 安全")
el2.clear()
el2.send_keys("8uhb*UHB")
el3 = driver.find_element_by_accessibility_id("登录")
el3.click()

#等待
time.sleep(10)

driver.quit()