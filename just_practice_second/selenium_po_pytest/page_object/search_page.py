from selenium.webdriver.common.by import By
from just_practice_second.selenium_po_pytest.base.base_page import Base


class Search(Base):
    el_search_input=(By.ID,"kw")
    el_search_bn=(By.ID,"su")

    def search_input(self,txt):
        self.send_keys(txt,*self.el_search_input)

    def search_click(self):
        self.click(*self.el_search_bn)

    def search_function(self,txt):
        self.search_input(txt)
        self.search_click()
