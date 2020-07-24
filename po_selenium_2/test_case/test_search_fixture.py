from po_selenium_2.page_object.search_page import Search
import pytest


@pytest.mark.usefixtures("before")  # 这种方式可以直接放在class前，也可以放在function前
class TestSearch:
    '''
    @pytest.mark.usefixtures("get_driver","open_yield")  #这种方式拿不到返回值
    @pytest.mark.parametrize("txt",["selenium","appium"])
    def test_01_search(self,txt,get_driver):
        search=Search(get_driver)
        search.visit(url="http://www.baidu.com")
        search.search_function(txt)
    '''

    # @pytest.mark.skip
    @pytest.mark.parametrize("txt", ["selenium", "appium"])
    def test_01_search(self, txt, open_addfinalizer):
        search = Search(open_addfinalizer)
        search.visit(url="http://www.baidu.com")
        search.search_function(txt)

    def test_02_register(self,register):
        print(f"注册信息是:{register}")

    def test_03_login(self,login):
        print(f"登录信息是:{login}")

    @pytest.mark.skip
    def test_04_test(self):
        assert 0

