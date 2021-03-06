from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from po_appium_1.base.base_page import BasePage
from po_appium_1.page_object.personal_page import PersonalPage
from po_appium_1.page_object.settings_page import SettingsPage
from po_appium_1.page_object.common_page import CommonPage


class LoginPage(BasePage):
    #元素
    el_custom_login_enter=(By.ID,"com.dangdang.reader:id/custom_login_tv")
    el_name_input=(By.ID,"com.dangdang.reader:id/name_edit")
    el_pw_input=(By.ID,"com.dangdang.reader:id/password_et")
    el_login_bn=(By.ID,"com.dangdang.reader:id/login_tv")
    el_private_switch=(By.ID,"com.dangdang.reader:id/private_switch_btn")

    def custom_login_enter(self):
        self.click(*PersonalPage.el_tab_personal)  #由于传入的是2个参数，此处定义的是不定长，别忘了*
        self.swipe_down()  # 防止页面不再最上方
        self.click(*PersonalPage.el_nickname)
        try:
            if self.is_displayed(*self.el_custom_login_enter):
                # print("找到账号密码登录入口！")
                self.logger.info("找到账号密码登录入口！")
                self.click(*self.el_custom_login_enter)
        except NoSuchElementException:
            # print("没有找到账号密码登录入口，可能默认已经进入了该页面。")
            self.logger.info("没有找到账号密码登录入口，可能默认已经进入了该页面。")

    def custom_login(self,account,pw,toast):
        self.custom_login_enter()  #这个函数调用可以写在这里，也可以写在test case中
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

        try:
            text = self.get_toast(toast)
            assert text   #直接用是否获取到正确的toast来断言

            if str(text).__contains__("登录成功"):
                self.logger.info("已登录成功!")
            else:
                self.logger.info("未登录成功!")
        except AssertionError:
            self.logger.error("没有获取到登录toast!")
        finally:
            if self.is_displayed(*self.el_name_input):
                self.logger.info("还停留在登录页面，手动返回！")
                self.click(*CommonPage.el_back_bn_login)


        # 以下用元素是否存在的方式判断，改成以上用toast来判断
        # try:
        #     if self.is_displayed(*self.el_name_input):
        #         self.click(*Common.el_back_bn_login)
        #         self.logger.info("还停留在登录页，未登录成功，手动返回。")
        # except NoSuchElementException:
        #     self.logger.info("已经离开登录页面，可能已经登录成功。")



