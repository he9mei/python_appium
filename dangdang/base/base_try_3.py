import time
from appium import webdriver

caps = {"automationName": "Appium", "platformName": "Android", "platformVersion": "8.0.0",
            "deviceName": "HMKNW17727007061", "appPackage": "com.dangdang.reader",
            "appActivity": ".activity.GuideActivity", "noReset": True}

class BasePre:
    driver = None

    def setup_class(self):
        # 启动driver
        global driver
        # driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        print("driver在class执行之前启动")
        driver=self.driver
        print("self.driver的值是：", self.driver)
        print("driver的值是：",driver)

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()
        print("driver在class执行完毕之后关闭")

    @staticmethod
    def get_driver():
        print("得到driver:",driver)
        return driver


'''
#用继承的方式得到的还是none
class GetDriver(BasePre):
    def get_driver(self):
        print("得到driver:", self.driver)
        return self.driver
'''