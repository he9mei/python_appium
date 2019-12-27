
import pytest
from appium import webdriver
from time import sleep

import logging
import logging.config


caps = {
    "automationName": "Appium",
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

#log配置有三种方法
'''
1.将配置写在log.conf配置文件，然后再读取配置返回logger。此处是写入fixture，用例直接将其传入。---未实现写入不同的文件名
2.将配置写在代码中，然后再调用。好处是可以自己定义文件名，方便不同的类或者方法中的log写入不同文件。
3.将配置写在py文件中，使用logging.basicConfig设置配置，传入level、filename、format等，不传入filename就会控制台输出。
'''

@pytest.fixture(scope="module")
def logger():
    CONF_LOG = "../log.conf"
    logging.config.fileConfig(CONF_LOG)
    logger = logging.getLogger()
    print("---打印日志---")
    return logger