from dangdang.base.global_val import gol
from selenium import webdriver

class DriverInit:
    def init(self):
        caps = {"automationName": "Appium", "platformName": "Android", "platformVersion": "8.0.0",
                    "deviceName": "HMKNW17727007061", "appPackage": "com.dangdang.reader",
                    "appActivity": ".activity.GuideActivity", "noReset": True}
        gol.init()
        gol.set_value("driver",webdriver.Remote("http://localhost:4723/wd/hub", caps))
