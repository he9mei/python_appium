from selenium.webdriver.common.by import By
from po_selenium_1.base.base_page import Base
from time import sleep

class Search(Base):
    #定位元素
    search_input_box=(By.ID,"kw")
    search_button=(By.ID,"su")

    def input_text(self,text):
        self.locator_element(*self.search_input_box).send_keys(text)

    def click_button(self):
        self.locator_element(*self.search_button).click()

    def search_text(self,url,text):
        self.open_browser(url)
        self.input_text(text)
        self.click_button()
        sleep(1)
'''
#也可以进一步把搜索功能写成一个函数，测试用例中直接调用，类似于一个关键字。
#当然也可以测试用例中再写。
#如果多个测试用例都需要搜索功能的化，为了避免代码冗余就可以这样写。
'''



