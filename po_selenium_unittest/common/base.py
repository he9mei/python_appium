# encoding=utf-8
from selenium import webdriver
from time import sleep
import unittest


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        print("启动driver")
        cls.driver.get("http://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()   # 貌似有问题，但是能用
        print("关闭driver")

    def get_locator(self, *el):
        self.driver.find_element(*el)

    def click(self, *el):
        self.get_locator(*el).click()  #AttributeError: 'NoneType' object has no attribute 'click'
        # self.driver.find_element(*el).click()

    def send_keys(self, search_key, *el):
        self.driver.find_element(*el).clear()
        self.driver.find_element(*el).send_keys(search_key)