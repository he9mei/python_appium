
import os

import pytest
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

from dangdang.base.base_try_3 import BasePre  #导入包时应该from到py文件
from dangdang.pages.login_page import ElementLogin
from dangdang.method.method_try import AppiumMethod


class TestLogin(BasePre):
    '''
    def init(self):
        global driver
        # global method
        driver = BasePre.get_driver()
        # method = AppiumMethod()
    '''
    def test_01(self):
        #进入登录页面
        # 可以通过继承父类属性的方式获得self.driver，(用继承获取的化，需要父类也要定义self.driver)
        # 也可以通过自己写的get_driver方法，
        # 但是都需要在set_up执行之后，driver才会被赋予已经启动的driver的值，不可重复启动
        global driver, method
        # driver=self.driver
        driver=BasePre.get_driver()
        method = AppiumMethod()
        #AppiumMethod需要实例化一次才能得到driver的值，因为我把获取driver的方法写在AppiumMethod构造方法中了

        # driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv").click()
        # el="com.dangdang.reader:id/tab_personal_iv"
        # driver.find_element_by_id(el).click()
        # driver.find_element_by_id(ElementLogin.id_tab_personal).click()
        # driver.find_element(By.ID,ElementLogin.id_tab_personal).click()
        # AppiumMethod.click_by_id(driver,ElementLogin.id_tab_personal)
        # AppiumMethod.click_by_id(ElementLogin.id_tab_personal)
        # AppiumMethod().click_by_id(ElementLogin.id_tab_personal)
        # AppiumMethod().click_by_id("com.dangdang.reader:id/tab_personal_iv")
        method.click_by_id(ElementLogin.id_tab_personal)
        driver.find_element_by_id("com.dangdang.reader:id/nickname_tv").click()
        # AppiumMethod().click_by_id(driver,value=ElementLogin.id_nickname_input)

    @pytest.mark.skip()
    def test_02(self):
        # driver = self.driver  #在第1个用例申明driver为global，则后面无需再定义
        # 默认如果没有进入账号密码登录，先点击账号密码登录
        try:
            el_pw_login = driver.find_element_by_id("com.dangdang.reader:id/custom_login_tv")
            if el_pw_login .is_displayed():
                print("默认进入短信验证码登录，找到了账号登录按钮！")
                el_pw_login .click()
        # except Exception as e:  #如果不打印异常会提示异常太宽泛
        except NoSuchElementException:
            print("可能默认就是账号密码登录！")
            # print(e)
        
        # 切换输入法
        os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")

        el_name_input=driver.find_element_by_id("com.dangdang.reader:id/name_edit")
        el_name_input.clear()
        el_name_input.send_keys("18500000005")
        el_pw_input = driver.find_element_by_id("com.dangdang.reader:id/password_et")
        el_pw_input.clear()
        el_pw_input.send_keys("111111")

        # 遇到问题：输入之后，键盘没有关闭，挡住了登录按钮
        driver.press_keycode(4)  #通过强制返回关闭键盘
        # driver.hide_keyboard()   # appium自己有关闭键盘的方法
        # ---此处用此方法报错Soft keyboard not present, cannot hide keyboard

        driver.find_element_by_id("com.dangdang.reader:id/login_tv").click()


