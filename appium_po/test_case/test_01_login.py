from appium_po.page_object.login_page import Login
from appium_po.page_object.settings_page import Settings
import pytest


class TestLogin(object):

    # @pytest.mark.parametrize("account,pw",[("18500228275","111111"),("hhm1@163.com","111111")])
    @pytest.mark.parametrize("account,pw", [("18500228275", "111111")])
    def test_1_custom_login(self,driver,account,pw):
        # print(f"获得conftest.py的driver是：{driver}")
        login=Login(driver)
        settings = Settings(driver)
        settings.logout()
        login.custom_login_enter()
        # login.custom_login("18500228275","111111")
        login.custom_login(account,pw)


if __name__=="__main__":
    pytest.main("-s -v --html=./report.html test_01_login.py")
'''
先进入appium_po路径
之前在selenium_po路径
-->cd ..
-->cd appium_po
'''