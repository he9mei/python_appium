from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from appium_po.base.base_page import Base
from appium_po.page_object.personal_page import Personal
from appium_po.page_object.settings_page import Settings

class Login(Base):
    #元素
    el_custom_login_enter=(By.ID,"com.dangdang.reader:id/custom_login_tv")
    el_name_input=(By.ID,"com.dangdang.reader:id/name_edit")
    el_pw_input=(By.ID,"com.dangdang.reader:id/password_et")
    el_login_bn=(By.ID,"com.dangdang.reader:id/login_tv")
    el_private_switch=(By.ID,"com.dangdang.reader:id/private_switch_btn")

    def custom_login_enter(self):
        self.click(*Personal.el_tab_personal)  #由于传入的是2个参数，此处定义的是不定长，别忘了*
        self.click(*Personal.el_nickname)
        try:
            if self.is_displayed(*self.el_custom_login_enter):
                print("找到账号密码登录入口！")
                self.click(*self.el_custom_login_enter)
        except NoSuchElementException:
            print("没有找到账号密码登录入口，可能默认已经进入了该页面。")

    def custom_login(self,account,pw):
        self.send_keys(account, *self.el_name_input)
        self.send_keys(pw, *self.el_pw_input)
        # self.driver.press_keycode(4)  #华为手机点击登录时虚拟键盘没有自动关闭，乐蒙手机是好的
        self.click(*self.el_private_switch)  # 新版本需要勾选
        self.click(*self.el_login_bn)