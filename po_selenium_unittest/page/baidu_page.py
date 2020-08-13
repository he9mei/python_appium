# encoding=utf-8
from selenium.webdriver.common.by import By
from po_selenium_unittest.common.base import Base


class SearchPage(Base):
    el_search_box = (By.ID, "kw")
    el_search_bn = (By.CSS_SELECTOR, "#su")

    # 如果只写元素定位，不写关键字，则可以不用driver和公共方法，可以不用继承Base
    # 如果需要写关键字驱动，则需要driver和公共方法，继承base
    def search(self, search_key):
        self.send_keys(search_key, *self.el_search_box)
        self.click(*self.el_search_bn)