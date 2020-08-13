# encoding=utf-8
from po_selenium_unittest.common.base import Base
from po_selenium_unittest.page.baidu_page import SearchPage
from selenium.webdriver.common.by import By
import unittest
from time import sleep


class TestSearch(Base):
    def test_1_search_(self):
        bp = SearchPage()
        # self.driver.find_element(By.ID,"kw").send_keys("selenium")
        # self.driver.find_element(*bp.el_search_bn).click()
        search_key = "selenium"
        self.send_keys(search_key, *bp.el_search_box)
        self.click(*bp.el_search_bn)
        sleep(2)

    def test_2_search(self):
        bp = SearchPage()
        search_key = "python"
        self.send_keys(search_key, *bp.el_search_box)
        self.click(*bp.el_search_bn)

    if __name__ == "__main__":
        unittest.main()


# 如果需要在testcase中写具体的操作步骤，则需要driver和公共方法，需要继承Base
# 如果全部用关键字，则可以只继承unittest.TestCase