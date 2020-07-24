import os
import time

from appium import webdriver

'''
caps = {}
caps["automationName"] = "XCUITest"
caps["platformName"] = "iOS"
caps["platformVersion"] = "12.4.5"
caps["deviceName"] = "iPhone 6 Plus"
caps["bundleId"] = "com.dangdang.DDReaderEbook"
caps["udid"] = "d3f1c7734e7d5124ed7b462fe14be64a0c22b65e"
caps["noReset"] = "true"
'''

'''
caps = {
    "automationName": "XCUITest",
    "platformName": "ios",
    "platformVersion": "12.4.5",
    "deviceName": "iPhone 6 Plus",
    "udid": "d3f1c7734e7d5124ed7b462fe14be64a0c22b65e",
    "bundleId": "com.dangdang.DDReaderEbook",
    "noRest": "true"
}
'''
caps = {
    "automationName": "XCUITest",
    "platformName": "ios",
    "platformVersion": "12.1",
    "deviceName": "iPhone 8",
    "udid": "86976FD8-4F7A-4949-A9D4-833FA3BBF88D",
    "bundleId": "com.dangdang.DDReaderEbook",
    "noRest": "true"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# 隐式等待
driver.implicitly_wait(10)

el1 = driver.find_element_by_xpath('//XCUIElementTypeOther[@name="我的"]')
el1.click()
el2 = driver.find_element_by_xpath('//XCUIElementTypeTable[@name="tableView"]/XCUIElementTypeCell[1]')
el2.click()
# 默认没有进入账号密码登录，先点击账号密码登录
el3=driver.find_element_by_accessibility_id('账号密码登录')
el3.click()

# 切换输入法---这是android的操作
# os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")

el4 = driver.find_element_by_xpath('//XCUIElementTypeOther[@name="root"]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField')
el4.clear()
el4.send_keys("18500000005")
el5 = driver.find_element_by_xpath('//XCUIElementTypeOther[@name="root"]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField')
el5.clear()
el5.send_keys("111111")

el6 = driver.find_element_by_accessibility_id('privacy gouxuan u')
el6.click()

el7 = driver.find_element_by_accessibility_id('登录')
el7.click()

# 等待
time.sleep(5)

driver.quit()