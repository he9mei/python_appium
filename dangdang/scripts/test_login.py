
import os

import pytest
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By

from dangdang.base.base2 import BasePre  #导入包时应该from到py文件
from dangdang.pages.login_page import ElementLogin
from dangdang.method.method import AppiumMethod

class TestLogin(BasePre):

    def test_01(self):
        #进入登录页面
        # driver=self.driver
        # driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv").click()
        # el="com.dangdang.reader:id/tab_personal_iv"
        # driver.find_element_by_id(el).click()
        # driver.find_element_by_id(ElementLogin.id_tab_personal).click()
        # driver.find_element(By.ID,ElementLogin.id_tab_personal).click()
        # AppiumMethod.click_by_id(ElementLogin.id_tab_personal)
        AppiumMethod.click_by_id(ElementLogin.id_tab_personal)
        # driver.find_element_by_id("com.dangdang.reader:id/nickname_tv").click()
        AppiumMethod.click_by_id(ElementLogin.id_nickname_input)

    @pytest.mark.skip()
    def test_02(self):
        driver = self.driver
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
        driver.press_keycode(4)

        driver.find_element_by_id("com.dangdang.reader:id/login_tv").click()


