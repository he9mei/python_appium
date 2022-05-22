import os
import time

from appium import webdriver

caps = {}
caps["automationName"] = "Appium"
# caps["aotomationName"] = "UIAutomator2"
caps["platformName"] = "Android"
# caps["platformVersion"] = "8.0.0"  #huawei
# caps["deviceName"] = "HMKNW17727007061"
caps["platformVersion"] = "10"  #oppo
caps["deviceName"]="GEY6R20507024610"  # adb devices
caps["appPackage"] = "com.dangdang.reader"  # adb shell pm list package|findstr dangdang
caps["appActivity"] = ".activity.GuideActivity"  # adb shell dumpsys activity|findstr com.dangdang.reader|findstr LAUNCHER
caps["noReset"] = True
#新增两个
caps["unicodeKeyboard"] = True  # appium默认不支持中文，这里表示启用unicode输入法
caps["resetKeyboard"] = True  # 测试结束后，重置输入法到原有状态

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#隐式等待
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv")
# el1 = driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]')
# el1 = driver.find_element_by_android_uiautomator('new UiSelector().text("我的")')
el1.click()
el2 = driver.find_element_by_android_uiautomator('new UiSelector().text("收藏")')
el2.click()



#等待
time.sleep(5)

driver.quit()