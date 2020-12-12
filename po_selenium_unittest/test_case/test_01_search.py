# encoding=utf-8
from po_selenium_unittest.base.base import Base
from po_selenium_unittest.page.search_page import SearchPage
from selenium.webdriver.common.by import By
import unittest
from time import sleep
from po_selenium_unittest.web_config import search_url


class TestSearch(Base):
    def test_1_search(self):
        sp = SearchPage()
        # self.visit(search_url)
        # self.driver.find_element(By.ID,"kw").send_keys("selenium")
        # self.driver.find_element(*bp.el_search_bn).click()
        search_key = "selenium"
        self.send_keys(search_key, *sp.el_search_box)
        self.click(*sp.el_search_bn)
        sleep(2)

    def test_2_search(self):
        sp = SearchPage()
        # self.visit(search_url)
        search_key = "python"
        self.send_keys(search_key, *sp.el_search_box)
        self.click(*sp.el_search_bn)

    if __name__ == "__main__":
        unittest.main()


# 如果需要在testcase中写具体的操作步骤，则需要driver和公共方法，需要继承Base