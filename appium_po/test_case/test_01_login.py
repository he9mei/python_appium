from appium_po.page_object.login_page import Login
from appium_po.page_object.settings_page import Settings
import pytest


class TestLogin(object):
    @pytest.mark.parametrize("account,pw,toast",[("","","请输入用户名"),("18500228275","","请输入密码"),("12345678901","111111","用户名或密码输入错误"),("18500228275","000000","用户名或密码输入错误"),("18500000099","111111","该用户名不存在"),("18500228275","111111","登录成功")])
    # @pytest.mark.parametrize("account,pw",[("",""),("18500228275",""),("12345678901","111111"),("18500228275","000000"),("18500228275","111111")])
    # @pytest.mark.parametrize("account,pw",[("18500228275","111111"),("hhm1@163.com","111111")])
    # @pytest.mark.parametrize("account,pw", [("18500228275", "111111")])
    def test_1_custom_login(self,driver,logger,account,pw,toast):
        logger.info("---测试登录流程---")
        # print(f"获得conftest.py的driver是：{driver}")
        login=Login(driver,logger)
        settings = Settings(driver,logger)
        settings.logout()
        login.custom_login_enter()
        # login.custom_login("18500228275","111111")
        # login.custom_login(account,pw)
        login.custom_login(account,pw,toast)  #把toast也参数化


if __name__=="__main__":
    pytest.main("-s -v --html=./report/report.html test_01_login.py")
'''
先进入appium_po路径
之前在selenium_po路径
-->cd ..
-->cd appium_po
'''