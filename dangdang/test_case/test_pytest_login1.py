
import time
import os
import pytest
from appium import webdriver


def setup_module():
    #启动driver
    caps = {"automationName": "Appium", "platformName": "Android", "platformVersion": "8.0.0",
            "deviceName": "HMKNW17727007061", "appPackage": "com.dangdang.reader",
            "appActivity": ".activity.GuideActivity", "noReset": True}
    global driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(10)
    print("driver在py文件执行之前启动")


def teardown_module():
    time.sleep(5)
    driver.quit()
    print("driver在py文件执行完毕之后关闭")


def test_01():
    #进入登录页面
    driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv").click()
    driver.find_element_by_id("com.dangdang.reader:id/nickname_tv").click()


# @pytest.mark.skip()
def test_02():
    # 默认如果没有进入账号密码登录，先点击账号密码登录
    try:
        el_pw_login = driver.find_element_by_id("com.dangdang.reader:id/custom_login_tv")
        if el_pw_login .is_displayed():
            print("默认进入短信验证码登录，找到了账号登录按钮！")
            el_pw_login .click()
    except Exception as e:  #如果不打印异常会提示异常太宽泛
        print("可能默认就是账号密码登录！")
        print(e)

    # 切换输入法
    os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")

    el_name_input=driver.find_element_by_id("com.dangdang.reader:id/name_edit")
    el_name_input.clear()
    el_name_input.send_keys("18500000005")
    el_pw_input = driver.find_element_by_id("com.dangdang.reader:id/password_et")
    el_pw_input.clear()
    el_pw_input.send_keys("111111")

    # 遇到问题：输入之后，键盘没有关闭，挡住了登录按钮
    driver.press_keycode(4)

    driver.find_element_by_id("com.dangdang.reader:id/login_tv").click()

'''
import os
import time

from appium import webdriver

caps = {}
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "8.0.0"
caps["deviceName"] = "HMKNW17727007061"
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

#遇到问题：输入之后，键盘没有关闭，挡住了登录按钮
driver.press_keycode(4)

el5 = driver.find_element_by_id("com.dangdang.reader:id/login_tv")
el5.click()

#等待
time.sleep(5)

driver.quit()
'''




