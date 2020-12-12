# encoding=utf-8

from po_selenium_unittest.base.base import Base
from po_selenium_unittest.page.search_page import SearchPage
from selenium.webdriver.common.by import By
import unittest
from time import sleep


class TestSearch(Base):
    def test_1_search(self):
        sp = SearchPage(self.driver)
        # 如果不传入diver，调用SearchPage的方法时，总是报错：没有driver属性。报错尝试
        # sp.enter_page()
        sp.search(search_key="unittest")

    def test_2_search(self):
        sp = SearchPage(self.driver)
        # sp.enter_page()
        search_key = "pytest"
        sp.search(search_key)

    if __name__ == "__main__":
        unittest.main()




# 如果需要在testcase中写具体的操作步骤，则需要driver和公共方法，需要继承Base
# 如果全部用关键字，则可以只继承unittest.TestCase-----不行，因为setup和tearown也写在了Base中

# 问题：
# test_1_search目前可以正常执行，test_2_search调用SearchPage的方法时，总是报错