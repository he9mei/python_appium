'''
参数化-DDT
1.@data时直接传入测试数据，如
# @data(("case1","selenium"),("case2","appium"))
# @data(["case1","selenium"],["case2","appium"])
@data({"search_key":"selenium"},{"search_key":"appium"})
@unpack

2.把测试数据写在文件中

'''

import unittest
from selenium import webdriver
import time
from ddt import ddt,data,file_data,unpack


@ddt
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

    # @data(("case1","selenium"),("case2","appium"))
    # @data(["case1","selenium"],["case2","appium"])
    @data({"search_key":"selenium"},{"search_key":"appium"})
    @unpack
    # def test_search(self,name,search_key):
    def test_search(self,search_key):
        '''百度搜索'''
        self.baidu_search(search_key)
        # self.assertEqual(self.driver.title,search_key+"_百度搜索")
        print("搜索词是：",search_key)
        self.assertEqual(self.driver.title, "百度一下，你就知道")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        print("关闭driver")


if __name__ == "__main__":
    unittest.main(verbosity=2)