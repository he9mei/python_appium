import os
import time

from appium import webdriver

caps = {}
# caps["automationName"] = "Appium"
caps["aotomationName"] = "UIAutomator2"
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

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
#隐式等待
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv")
el1.click()
el2 = driver.find_element_by_id("com.dangdang.reader:id/nickname_tv")
el2.click()
#默认没有进入账号密码登录，先点击账号密码登录
driver.find_element_by_id("com.dangdang.reader:id/custom_login_tv").click()

#切换输入法
# os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")
#补充：以上driver新增了启动unicode,此处则可以省略了

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
time.sleep(5)

driver.quit()