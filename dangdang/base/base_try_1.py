import time
from appium import webdriver

driver = None

class BasePre:
    @staticmethod
    def setup_class():
        # 启动driver

        caps = {"automationName": "Appium", "platformName": "Android", "platformVersion": "8.0.0",
                "deviceName": "HMKNW17727007061", "appPackage": "com.dangdang.reader",
                "appActivity": ".activity.GuideActivity", "noReset": True}
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        driver.implicity_wait(10)
        
        print("driver在py文件执行之前启动")

    @staticmethod
    def teardown_class(self):
        time.sleep(5)
        driver.quit()
        print("driver在py文件执行完毕之后关闭")
