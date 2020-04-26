from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from po_appium.base.base_page import Base
from po_appium.page_object.personal_page import Personal
from po_appium.page_object.settings_page import Settings
from po_appium.page_object.common_page import Common


class Login(Base):
    #元素
    el_custom_login_enter=(By.ID,"com.dangdang.reader:id/custom_login_tv")
    el_name_input=(By.ID,"com.dangdang.reader:id/name_edit")
    el_pw_input=(By.ID,"com.dangdang.reader:id/password_et")
    el_login_bn=(By.ID,"com.dangdang.reader:id/login_tv")
    el_private_switch=(By.ID,"com.dangdang.reader:id/private_switch_btn")

    def custom_login_enter(self):
        self.swipe_down()   #防止页面不再最上方
        self.click(*Personal.el_tab_personal)  #由于传入的是2个参数，此处定义的是不定长，别忘了*
        self.click(*Personal.el_nickname)
        try:
            if self.is_displayed(*self.el_custom_login_enter):
                # print("找到账号密码登录入口！")
                self.logger.info("找到账号密码登录入口！")
                self.click(*self.el_custom_login_enter)
        except NoSuchElementException:
            # print("没有找到账号密码登录入口，可能默认已经进入了该页面。")
            self.logger.info("没有找到账号密码登录入口，可能默认已经进入了该页面。")

    def custom_login(self,account,pw,toast):
        '''
        # 不验证toast的登录
        self.send_keys(account, *self.el_name_input)
        self.send_keys(pw, *self.el_pw_input)
        # self.driver.press_keycode(4)  #华为手机点击登录时虚拟键盘没有自动关闭，乐蒙手机是好的
        self.click(*self.el_private_switch)  # 新版本需要勾选
        self.click(*self.el_login_bn)
        '''

        '''
        # 验证获取toast的登录
        # 暂无法做到参数化+不合法/不正确账号密码时toast的验证，因为获取toast需要传入部分文字获取全部文字，
        # 但参数化时需要的部分文字是不同的。除非，把toast需要传入的部分文字也一起参数化。
        self.wait(2)
        self.click(*self.el_login_bn)
        self.get_toast("请输入用户名")
        self.send_keys(account, *self.el_name_input)
        self.click(*self.el_login_bn)
        self.get_toast("请输入密码")
        self.send_keys(pw, *self.el_pw_input)
        self.click(*self.el_login_bn)
        self.get_toast("请先勾选同意")
        self.click(*self.el_private_switch)
        self.click(*self.el_login_bn)
        self.get_toast("登录成功")
        '''

        '''
        # 不验证toast的登录，参数化
        self.send_keys(account, *self.el_name_input)
        self.send_keys(pw, *self.el_pw_input)
        # self.driver.press_keycode(4)  #华为手机点击登录时虚拟键盘没有自动关闭，乐蒙手机是好的
        self.click(*self.el_private_switch)  # 新版本需要勾选
        self.click(*self.el_login_bn)
        # self.get_screenshot("login_"+account+"_"+pw)  #截图不一定能截到toast
        self.logger.info("正在登录："+account+","+pw)
        try:
            if self.is_displayed(*self.el_name_input):
                self.click(*Common.el_back_bn_login)
                self.logger.info("还停留在登录页，未登录成功，手动返回。")
        except NoSuchElementException:
            self.logger.info("已经离开登录页面，可能已经登录成功。")
            '''

        # 验证toast的登录，参数化
        self.send_keys(account, *self.el_name_input)
        self.send_keys(pw, *self.el_pw_input)
        # self.driver.press_keycode(4)  #华为手机点击登录时虚拟键盘没有自动关闭，乐蒙手机是好的
        self.click(*self.el_private_switch)  # 新版本需要勾选
        self.click(*self.el_login_bn)
        self.logger.info("正在登录：" + account + "," + pw)
        self.get_toast(toast)
        try:
            if self.is_displayed(*self.el_name_input):
                self.click(*Common.el_back_bn_login)
                self.logger.info("还停留在登录页，未登录成功，手动返回。")
        except NoSuchElementException:
            self.logger.info("已经离开登录页面，可能已经登录成功。")



