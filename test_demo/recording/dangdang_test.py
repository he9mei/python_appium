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
caps["appPackage"] = "com.dangdang.reader"
caps["appActivity"] = ".activity.GuideActivity"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

#隐式等待
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]")
el2.click()
el3 = driver.find_element_by_id("com.dangdang.reader:id/custom_login_tv")
el3.click()
el4 = driver.find_element_by_id("com.dangdang.reader:id/name_edit")
el4.send_keys("18500000006")
el5 = driver.find_element_by_id("com.dangdang.reader:id/password_et")
el5.send_keys("111111")
el6 = driver.find_element_by_id("com.dangdang.reader:id/login_tv")
el6.click()

#等待
time.sleep(10)

driver.quit()