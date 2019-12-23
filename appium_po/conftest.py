
import pytest
from appium import webdriver
from time import sleep

caps = {
    "automationName":"Appium",
    "platformName":"Android",
    "platformVersion":"8.0.0",
    "deviceName":"HMKNW17727007061",
    "appPackage":"com.dangdang.reader",  #adb shell pm list package -3
    "appActicity":".activity.GuideActivity",  #adb shell dumpsys activity |grep com.dangdang.reader |grep LAUNCHER
    "noReset": True}


@pytest.fixture(scope="session")
def driver(request):
    driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
    driver.implicitly_wait(10)
    print("启动driver")

    def end():
        driver.qiut()
        sleep(5)

    request.addfinalizer(end)
    return driver





