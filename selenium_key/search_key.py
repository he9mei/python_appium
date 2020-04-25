from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class KeyDemo:
    def open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def visit(self,url):
       self.driver.get(url)

    def locator(self,*locator):
        el=self.driver.find_element(*locator)
        return el

    def send_keys(self,txt,*locator):
        # self.driver.find_element_by_id(id).send_keys(txt)
        self.locator(*locator).send_keys(txt)

    def click(self,*locator):
        # self.driver.find_element_by_id(id).click()
        self.locator(*locator).click()

    def quit(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    el_baidu_input=(By.ID,"kw")
    el_baidu_bn=(By.ID,"su")
    key = KeyDemo()
    key.open_browser()
    key.visit("http://www.baidu.com")
    # key.send_keys("selenium", "kw")
    key.send_keys("selenium",*el_baidu_input)   #注意传参时也需要加*
    # key.click("su")
    key.click(*el_baidu_bn)
    key.quit()
