
from appium import webdriver
from appium_po.conftest import caps
import os

class Base(object):
    def __init__(self,driver):
        self.driver=driver
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)

    def locator_element(self,*locator):
        '''定位元素'''
        el=self.driver.find_element(*locator)
        return el

    def click(self,*locator):
        self.locator_element(*locator).click()

    def send_keys(self,*locator,text):
        self.locator_element(*locator).clear()
        self.locator_element(*locator).send_keys(text)

    def input_method(self):
        os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")


