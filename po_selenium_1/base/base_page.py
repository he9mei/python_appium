
'''
conftest.py中的driver，需要class以Test开头，方法以test_开头，才能识别driver。此处识别不了。
直接传入driver，使用的时候即实例化的时候再传。但是有一个问题是写driver相关方法的时候无法自动弹出方法。
'''
# from selenium import webdriver

class Base(object):
    def __init__(self,driver):
        # self.driver=webdriver.Chrome()
        self.driver=driver
        # self.url=url

    #访问页面
    def open_browser(self,url):
        self.driver.get(url)

    #元素定位
    def locator_element(self,*locator):
        el=self.driver.find_element(*locator)
        return el







