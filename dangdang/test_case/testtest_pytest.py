import pytest
import time
from appium import webdriver

def setup_module():
    caps = {"automationName": "Appium", "platformName": "Android", "platformVersion": "8.0.0",
            "deviceName": "HMKNW17727007061", "appPackage": "com.dangdang.reader",
            "appActivity": ".activity.GuideActivity", "noReset": True}
    global driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicity_wait(10)
    print("driver已经启动")

def teardown_module():
        driver.quit()
        print("driver已经关闭")

class TestModule():
    def test_01(self):
        driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv").click()
        time.sleep(5)


