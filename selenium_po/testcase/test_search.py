from selenium_po.page_object.search_page import Search
import pytest


class TestSearch(object):

    def test_search(self,driver):
        url = "http://wwww.baidu.com"
        text = "selenium"

        s=Search(driver)
        # s.search_text(text)
        s.open_browser(url)
        s.input_text(text)
        s.click_button()

if __name__=="__main__":
    pytest.main("-s -v --html=./report/report.html test_search.py")
    #先cd selenium_po
    #完成路径为cd /Users/hehuaimei/PycharmProjects/python_appium/selenium_po

