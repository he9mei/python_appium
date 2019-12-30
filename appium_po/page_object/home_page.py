from appium_po.base.base_page import Base
from appium_po.page_object.personal_page import Personal
from appium_po.page_object.common_page import Common
from selenium.webdriver.common.by import By


class Home(Base):
    # 元素
    el_my_reading_list = (By.ID, "com.dangdang.reader:id/book_layout")
    el_my_bar_enter = (By.ID,"com.dangdang.reader:id/join_bar_count_tv")
    el_my_bar_list = (By.ID,"com.dangdang.reader:id/pay_rl")
    el_my_publish_list = (By.ID, "com.dangdang.reader:id/desc")

    def my_home_enter(self):
        self.click(*Personal.el_tab_personal)
        self.click(*Personal.el_nickname)
        self.explicitly_wait(10,self.el_my_reading_list)  #注意：此处元素参数不需要*，以元组形式传入,原方法可以直接接收元组
        self.get_screenshot("my_home_page")  #验证截图

    def my_bar(self):
        self.swipe_up_to_el(*self.el_my_bar_list)
        self.wait(1)
        self.click_index(0,*self.el_my_bar_list)
        self.wait(1)
        self.click(*Common.el_back_bn_bar)
        self.click_random(*self.el_my_bar_list)
        self.wait(1)
        self.click(*Common.el_back_bn_bar)

    def my_publish(self):
        self.swipe_up_to_el(*self.el_my_publish_list)  #元素貌似有问题，根本不滑动










