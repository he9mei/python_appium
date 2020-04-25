from selenium import webdriver
import time

class Base:
    def __init__(self,driver):
        self.driver=driver
        print(f"Base获取的driver是{self.driver}")

    # def open_browser(self):
    #     self.driver = webdriver.Chrome()

    def visit(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    # def quit(self):
    #     time.sleep(3)
    #     self.driver.quit()

    def locator_element(self,*locator):
        el=self.driver.find_element(*locator)
        return el

    def send_keys(self,txt,*locator):
        self.locator_element(*locator).send_keys(txt)

    def click(self,*locator):
        self.locator_element(*locator).click()
