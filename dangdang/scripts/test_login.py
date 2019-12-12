
import os

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from dangdang.base.base import BasePre
from dangdang.pages.login_page import ElementLogin
from dangdang.method.method import AppiumMethod


class TestLogin(BasePre):

    def test_01(self):
        global driver, method
        driver = BasePre.get_driver()
        method = AppiumMethod()

        # 进入登录页面
        method.click_by_id(ElementLogin.id_tab_personal)
        method.click(By.ID,ElementLogin.id_nickname_input)

    # @pytest.mark.skip()
    def test_02(self):
        # 默认如果没有进入账号密码登录，先点击账号密码登录
        try:
            el_pw_login = driver.find_element_by_id("com.dangdang.reader:id/custom_login_tv")
            if el_pw_login .is_displayed():
                print("默认进入短信验证码登录，找到了账号登录按钮！")
                el_pw_login .click()
        except NoSuchElementException:
            print("可能默认就是账号密码登录！")
        
        # 切换输入法
        os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")

        el_name_input=driver.find_element_by_id("com.dangdang.reader:id/name_edit")
        el_name_input.clear()
        el_name_input.send_keys("18500000005")
        el_pw_input = driver.find_element_by_id("com.dangdang.reader:id/password_et")
        el_pw_input.clear()
        el_pw_input.send_keys("111111")

        # 遇到问题：输入之后，键盘没有关闭，挡住了登录按钮
        driver.press_keycode(4)   # 通过强制返回关闭键盘

        driver.find_element_by_id("com.dangdang.reader:id/login_tv").click()


