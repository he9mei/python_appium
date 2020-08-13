# encoding=utf-8
from po_selenium_unittest.common.base import Base
from po_selenium_unittest.page.baidu_page import SearchPage
from selenium.webdriver.common.by import By
import unittest
from time import sleep


class TestSearch(Base):
    def test_1_search_(self):
        sp = SearchPage()
        sp.search(search_key="unittest")

    def test_2_search(self):
        sp = SearchPage()
        search_key = "pytest"
        sp.search(search_key)

    if __name__ == "__main__":
        unittest.main()


# 如果需要在testcase中写具体的操作步骤，则需要driver和公共方法，需要继承Base
# 如果全部用关键字，则可以只继承unittest.TestCase-----不行，因为setup和tearown也写在了Base中