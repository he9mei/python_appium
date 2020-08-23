# encoding=utf-8
from selenium.webdriver.common.by import By
from po_selenium_unittest.base.base import Base
from po_selenium_unittest.web_config import search_url


class SearchPage(Base):
    el_search_box = (By.ID, "kw")
    el_search_bn = (By.CSS_SELECTOR, "#su")

    # def __init__(self, driver):   # 报错尝试
    #     self.driver = driver

    # 如果只写元素定位，不写关键字，则可以不用driver和公共方法，可以不用继承Base
    # 如果需要写关键字驱动，则需要driver和公共方法，继承base
    def enter_page(self):
        self.visit(search_url)

    def search(self, search_key):
        self.send_keys(search_key, *self.el_search_box)
        self.click(*self.el_search_bn)