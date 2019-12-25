from appium_po.base.base_page import Base
from appium_po.page_object.personal_page import Personal
from selenium.webdriver.common.by import By

class Home(Base):
    # 元素---暂时没写
    el_my_reading_list = (By.ID, "com.dangdang.reader:id/book_layout")
    el_my_publish_list = (By.ID, "com.dangdang.reader:id/desc")

    def my_home_enter(self):
        self.click(*Personal.el_tab_personal)
        self.click(*Personal.el_nickname)
        self.explicitly_wait(10,self.el_my_reading_list)  #注意：此处不需要*，以元组形式传入

    def my_publish(self):
        # self.swipe_up_to_el(*self.el_my_reading_list)
        self.swipe_up()






