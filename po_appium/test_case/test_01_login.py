from po_appium.page_object.login_page import Login
from po_appium.page_object.settings_page import Settings
import pytest

from po_appium.base.logger import Logger
from pathlib import Path

logger=Logger().logger(Path(__file__).name)

'''
#pytest.mark.parametrize实现参数化，如果数据较多，也可以把数据单独写成一个元素列表或者字典列表，元组列表更简单一些。
#当然还可以写到excel文件中---暂未实现
login_data=[("","","请输入用户名"),
            ("18500228275","","请输入密码"),
            ("12345678901","111111","用户名或密码输入错误"),
            ("18500228275","000000","用户名或密码输入错误"),
            ("18500000099","111111","该用户名不存在"),
            ("18500228275","111111","登录成功")]
'''

class TestLogin(object):
    @pytest.mark.parametrize("account,pw,toast", [("18500228275", "111111", "登录成功")])
    # @pytest.mark.parametrize("data",login_data)
    # @pytest.mark.parametrize("account,pw,toast",[("","","请输入用户名"),
    #                                              ("18500228275","","请输入密码"),
    #                                              ("12345678901","111111","用户名或密码输入错误"),
    #                                              ("18500228275","000000","用户名或密码输入错误"),
    #                                              ("18500000099","111111","该用户名不存在"),
    #                                              ("18500228275","111111","登录成功")])
    # @pytest.mark.parametrize("account,pw",[("",""),("18500228275",""),("12345678901","111111"),("18500228275","000000"),("18500228275","111111")])
    # @pytest.mark.parametrize("account,pw",[("18500228275","111111"),("hhm1@163.com","111111")])
    # @pytest.mark.parametrize("account,pw", [("18500228275", "111111")])
    def test_01_custom_login(self,driver,account,pw,toast):  #此处去掉传入logger
    # def test_1_custom_login(self,driver,logger,data):
        logger.info("---测试登录流程---")
        # print(f"获得conftest.py的driver是：{driver}")
        login=Login(driver)  #此处去掉传入logger
        settings = Settings(driver)   #此处去掉传入logger
        settings.logout()
        login.custom_login_enter()
        # login.custom_login("18500228275","111111")
        # login.custom_login(account,pw)
        login.custom_login(account,pw,toast)  #把toast也参数化
        # login.custom_login(data[0],data[1],data[2])  #把数据单独写到元组列表，再获取数据

'''
if __name__=="__main__":
    pytest.main("-s -v --html=./report/report.html test_01_login.py")
    pytest.main("-s -v --alluredir=%allure_result_folder% test_01_login.py")
    #allure报告生成是具体到文件夹即可，无需到文件名---这里执行没有生成？
'''

'''
在pytest.main执行以上用例
先进入appium_po路径
之前在selenium_po路径
-->cd ..
-->cd po_appium

在terminal执行以上用例：
如果要在terminal执行pytest -s -v --alluredir=allure_report test_01_login.py
需要先进入-->cd ./test_case
此时allure_report放在test_case下了，统一放在result下：
-->pytest -s -v --alluredir=../test_result/report/allure_report test_01_login.py
打开时也需要对应的路径：
-->allure serve ../test_result/report/allure_report

如果要使用普通的报告：
-->pytest -s -v --html=../test_result/report/html_report/report.html test_01_login.py
'''

'''
最新修改：
//how to run case in terminal use this pytest.ini file
-->cd /Users/hehuaimei/PycharmProjects/python_appium/po_appium
-->pytest
//之后所有路径，都是以项目路径（即testcase上一级）为基础
//执行时，再指定用例testpaths=./test_case
'''