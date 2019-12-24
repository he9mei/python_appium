
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

from appium_po.conftest import caps
import os
from time import sleep

class Base(object):
    def __init__(self, driver):
        self.driver=driver
        # self.driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)
        print(f"传入Base的driver是：{self.driver}")

    def locator_element(self, *locator):
        '''定位元素'''
        try:
            el=self.driver.find_element(*locator)
            return el
        except NoSuchElementException:
            print(f"找不到元素：{locator}")

    def click(self, *locator):
        self.locator_element(*locator).click()
        print(f"点击元素:{locator}")

    def send_keys(self, text, *locator):
        self.sys_input_method("appiumUnicode")
        self.locator_element(*locator).clear()
        self.locator_element(*locator).send_keys(text)
        print(f"元素：{locator} 输入：{text}")
        # self.sys_input_method("baidu")  #输入之后切换到百度输入法，不切回去也行

    def is_displayed(self, *locator):
        try:
            # if self.driver.find_element(*locator).is_displayed():
            assert self.driver.find_element(*locator).is_displayed()
            # print("元素出现")
            return True
        # except NoSuchElementException:
        except AssertionError:
            print(f"元素未出现:{locator}")
            return False

    def sys_input_method(self, method_name):
        '''切换手机系统的输入法'''
        if method_name=="appiumUnicode":
            os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")
        if method_name=="baidu":
            os.system("adb shell ime set com.baidu.input_huawei/.ImeService")

    def swipe_up(self,n):
        s=self.driver.get_window_size()
        print(s)
        start_x = s['width']*1/2
        start_y = s['height']*2/5
        end_x = s['width']*1/2
        end_y = s['height']*1/5
        t = 500
        for i in range(n):
            self.driver.swipe(start_x,start_y,end_x,end_y,t)
            print(f"向上滑动{i+1}次")


