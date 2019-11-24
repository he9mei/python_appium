
from appium import webdriver
import unittest

caps = {"automationName": "Appium", "platformName": "Android", "platformVersion": "8.0.0",
            "deviceName": "HMKNW17727007061", "appPackage": "com.dangdang.reader",
            "appActivity": ".activity.GuideActivity"}

class BasePrepare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver=webdriver.remote("http://localhost:4723/wd/hub",caps)

    @classmethod
    def tearDownClass(cls):
        driver.quit()  # 无法调用局部变量




