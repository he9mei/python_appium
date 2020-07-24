from po_selenium_2.page_object.search_page import Search
import pytest
from selenium import webdriver
import time


class TestSearch:
    def setup_class(self):
       self.driver=webdriver.Chrome()

    def teardown_class(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("txt",["selenium","appium"])
    def test_01_search(self,txt):
        search=Search(self.driver)
        # search.open_browser()
        search.visit(url="http://www.baidu.com")
        search.search_function(txt)
        # search.search_function(txt)
        # search.quit()

'''
    @pytest.mark.skip
    # @pytest.mark.skipif(2>1,reason="条件为真，跳过")
    def test_02_skip(self):
        print("just test")

    # @pytest.mark.parametrize("username",["18500000001","1850000002"])
    # def test_03_para(self,username):
    #     print("账号是：{}".format(username))

    # @pytest.mark.parametrize(("username","pw"),[("18500000001","111111"),("18500000002","222222")])
    # def test_04_para(self,username,pw):
    #     print(f"账号是{username}密码是{pw}")

    # login_data=[("18500000001","111111"),
    #             ("18500000002","222222")]
    login_data=[{"username":"18500000001","pw":"111111"},
                {"username":"18500000002","pw":"222222"}]
    @pytest.mark.parametrize("data",login_data)
    def test_05_para(self,data):
        # print(f"账号是{data[0]}密码是{data[1]}")
        print("账号是"+data["username"]+"密码是"+data["pw"])  #用字典取值时，不能用格式化输出
'''

# if __name__=="__main__":
#     pytest.main("-s -v test_search.py --html=./report/report.html")


'''
遇到问题：
MAIN方法执行，一直没有得到报告
但是直接在terminal执行，可以得报告
先进入test_case目录下
-->pytest -s -v --html=./report/report.html
-->pytest -s -v --reruns=2
'''