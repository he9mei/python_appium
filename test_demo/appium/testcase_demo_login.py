import os
import time

from appium import webdriver

caps = {}
# caps["automationName"] = "Appium"
caps["aotomationName"] = "UIAutomator2"
caps["platformName"] = "Android"
# caps["platformVersion"] = "8.0.0"  #huawei
# caps["deviceName"] = "HMKNW17727007061"
caps["platformVersion"]="7.1.1"  #oppo
caps["deviceName"]="MJA68TGES4S4SKAY"
caps["appPackage"] = "com.dangdang.reader"
caps["appActivity"] = ".activity.GuideActivity"
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#隐式等待
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv")
el1.click()
el2 = driver.find_element_by_id("com.dangdang.reader:id/nickname_tv")
el2.click()
#默认没有进入账号密码登录，先点击账号密码登录
driver.find_element_by_id("com.dangdang.reader:id/custom_login_tv").click()

#切换输入法
os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")

el3 = driver.find_element_by_id("com.dangdang.reader:id/name_edit")
el3.clear()
el3.send_keys("18500000005")
el4 = driver.find_element_by_id("com.dangdang.reader:id/password_et")
el4.clear()
el4.send_keys("111111")

#部分手机遇到问题：输入之后，键盘没有关闭，挡住了登录按钮。
# driver.press_keycode(4)

el5 = driver.find_element_by_id("com.dangdang.reader:id/private_switch_btn")
el5.click()
el6 = driver.find_element_by_id("com.dangdang.reader:id/login_tv")
el6.click()

#等待
time.sleep(10)

driver.quit()