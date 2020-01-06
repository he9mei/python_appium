import unittest
from selenium import webdriver
import time


class TestBaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.base_url="http://wwww.baidu.com"
        print("启动driver")

    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()

    def test_search_selenium(self):
        '''百度搜索selenium'''
        search_key="selenium"
        self.baidu_search(search_key)
        # self.assertEqual(self.driver.title,search_key+"_百度搜索")
        self.assertEqual(self.driver.title, "百度一下，你就知道")
        time.sleep(2)

    def test_search_appium(self):
        '''百度搜索appium'''
        search_key="appium"
        self.baidu_search(search_key)
        # self.assertEqual(self.driver.title,search_key+"_百度搜索")
        self.assertEqual(self.driver.title, "百度一下，你就知道")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        print("关闭driver")


if __name__=="__main__":
    unittest.main()