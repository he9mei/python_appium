# encoding=utf-8
from selenium import webdriver
from time import sleep
import unittest
from po_selenium_unittest.web_config import browser


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = browser
        if cls.browser == "Chrome":
            cls.driver = webdriver.Chrome()
        print("启动driver")
        cls.driver.get("http://www.baidu.com")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()   # 貌似有问题，但是能用---不太明白
        print("关闭driver")

# 公共方法封装
    def visit(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def get_locator(self, *locator):
        el = self.driver.find_element(*locator)
        return el

    def click(self, *locator):
        self.get_locator(*locator).click()
        # 遇到问题：AttributeError: 'NoneType' object has no attribute 'click'
        # 原因：get_locator忘了return

    def send_keys(self, search_key, *locator):
        self.get_locator(*locator).clear()
        self.get_locator(*locator).send_keys(search_key)