import time
from appium import webdriver


class BasePre:
    driver = None

    # @staticmethod
    def setup_class(self):
        # 启动driver

        caps = {"automationName": "Appium", "platformName": "Android", "platformVersion": "8.0.0",
                "deviceName": "HMKNW17727007061", "appPackage": "com.dangdang.reader",
                "appActivity": ".activity.GuideActivity", "noReset": True}
        global driver
        # driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        print("driver在class执行之前启动")

    # @staticmethod
    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()
        print("driver在class执行完毕之后关闭")


