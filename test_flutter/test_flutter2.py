import os
import time

from appium import webdriver
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

caps = {}
# caps["automationName"] = "Appium"
# caps["aotomationName"] = "UIAutomator2"
caps['automationName'] = 'flutter'
caps["platformName"] = "Android"
# caps["platformVersion"] = "8.0.0"  #huawei
# caps["deviceName"] = "HMKNW17727007061"
caps["platformVersion"]="10"  #oppo
caps["deviceName"]="GEY6R20507024610"  # adb devices
caps["appPackage"] = "com.dangdang.reader"  # adb shell pm list package|findstr dangdang
caps["appActivity"] = ".activity.GuideActivity"  # adb shell dumpsys activity|findstr com.dangdang.reader|findstr LAUNCHER
caps["noReset"] = "True"
#新增两个
caps["unicodeKeyboard"]="True"   # appium默认不支持中文，这里表示启用unicode输入法
caps["resetKeyboard"]="True"   # 测试结束后，重置输入法到原有状态

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv").click()

# driver.execute("enableFlutterDriverExtension()")
finder = FlutterFinder()
text_finder = finder.by_text("收藏")
text_element = FlutterElement(driver, text_finder)
text_element.click()

# 等待
time.sleep(5)

driver.quit()