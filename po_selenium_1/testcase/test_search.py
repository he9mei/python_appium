from po_selenium_1.page_object.search_page import Search
import pytest
from time import sleep

class TestSearch(object):
    '''
    def test_search(self,driver):
        url = "http://wwww.baidu.com"
        text = "selenium"

        s=Search(driver)
        # s.search_text(text)
        s.open_browser(url)
        s.input_text(text)
        s.click_button()
    '''
    #实现text参数化
    @pytest.mark.parametrize("text",["selenium","appium"])
    def test_search(self, driver,text):
        url = "http://wwww.baidu.com"
        s = Search(driver)
        s.search_text(url,text)
        # s.open_browser(url)
        # s.input_text(text)
        # s.click_button()
        # sleep(1)

if __name__=="__main__":
    pytest.main("-s -v --html=./report/report.html test_search.py")
    #先cd po_selenium_1
    #完成路径为cd /Users/hehuaimei/PycharmProjects/python_appium/po_selenium_1

