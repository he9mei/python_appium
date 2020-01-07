'''
参数化-DDT
2.把测试数据写在文件中
（2）yaml文件
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

    @file_data("../data/ddt_baidu_data.yaml")
    def test_search(self,case):
        '''百度搜索'''
        search_key=case[0]["search_key"]
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

#注意：
# 如果py文件内用unittest.main()执行用例时，如果没有定位到这块代码，总是报错Empty suite