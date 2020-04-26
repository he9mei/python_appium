from appium import webdriver
import time

caps = {
    "automatonName": "Appium",
    "platformName": "android",
    "platformVersion": "6.0.1",
    "deviceName": "emulator-5554",  # adb devices
    "appPackage": "com.dangdang.reader",  # adb shell pm list package|findstr dangdang
    "appActivity": ".activity.GuideActivity",  # adb shell dumpsys activity|findstr com.dangdang.reader|findstr LAUNCHER
    "noReset": "true",
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.implicitly_wait(10)

# 具体用例简化
el1 = driver.find_element_by_id("id")
el1.click()

time.sleep(5)
driver.quit()
