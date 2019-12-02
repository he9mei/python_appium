from appium import webdriver

caps = {"automationName": "Appium", "platformName": "Android", "platformVersion": "8.0.0",
        "deviceName": "HMKNW17727007061", "appPackage": "com.dangdang.reader",
        "appActivity": ".activity.GuideActivity", "noReset": True}
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


class BasePrepare():

    @classmethod
    def set_up(cls):
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicity_wait(10)

    @classmethod
    def tear_down(cls):
        driver.quit()  # 无法调用局部变量,因此把driver申明为全局变量
