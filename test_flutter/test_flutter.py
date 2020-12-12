import unittest
from appium import webdriver
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

class FlutterTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'GEY6R20507024610'
        # desired_caps['app'] = r'D:\flutter_demo\build\app\outputs\apk\debug\app-debug.apk'
        desired_caps["appPackage"] = "com.dangdang.reader"  # adb shell pm list package|findstr dangdang
        desired_caps["appActivity"] = ".activity.GuideActivity"  # adb shell dumpsys activity|findstr com.dangdang.reader|findstr LAUNCHER
        # desired_caps['app'] = r'/Users/hehuaimei/Desktop/ddReader-7.0.7-online-debug_30000.apk'
        desired_caps["noReset"] = "True"
        desired_caps['automationName'] = 'flutter'
        # desired_caps['automationName'] = 'UiAutomator2'

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

        self.finder = FlutterFinder()

    def test_flutter(self):
        text_finder = self.finder.by_value_key("counter")
        button_finder = self.finder.by_value_key("increment")
        text_element = FlutterElement(self.driver, text_finder)
        button_element = FlutterElement(self.driver, button_finder)
        button_element.click()
        button_element.click()
        self.assertEqual('2',text_element.text)

    def tearDown(self):
        self.driver.quit()