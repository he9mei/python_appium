
import pytest
from appium import webdriver
from time import sleep

import logging
import logging.config


caps = {
    # "automationName": "Appium",
    "automationName": "UIAutomator2",
    "platformName": "Android",
    # "platformVersion": "8.0.0",  #华为手机
    # "deviceName": "HMKNW17727007061",
    # "platformVersion": "7.1.1",  #OPPO手机
    # "deviceName": "MJA68TGES4S4SKAY",
    "platformVersion": "5.1",  #乐蒙手机
    "deviceName": "MUGW8SOWWEY75NNDM",
    "appPackage": "com.dangdang.reader",  #adb shell pm list package -3
    "appActivity": ".activity.GuideActivity",  #adb shell dumpsys activity |grep com.dangdang.reader |grep LAUNCHER
    "noReset": True
}


@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
    driver.implicitly_wait(10)
    print("启动driver")

    def end():
        sleep(5)
        driver.quit()
        print("关闭driver")

    request.addfinalizer(end)
    return driver

'''
def test_1(driver):
    print("测试用例")


if __name__ == '__main__':
    pytest.main("-s conftest.py")
'''

'''
#也可以写成这种格式，先定义一个字典，再加数据
caps = {}
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "8.0.0"
caps["deviceName"] = "HMKNW17727007061"
caps["appPackage"] = "com.dangdang.reader"
caps["appActivity"] = ".activity.GuideActivity"
caps["noReset"] = "true"   #"true"或者True都可以，但是如果不写这个，每次启动都会清缓存重新启动
'''

@pytest.fixture(scope="session")
def logger():
    CONF_LOG = "../log.conf"
    logging.config.fileConfig(CONF_LOG)
    logger = logging.getLogger()
    print("---打印日志---")
    return logger