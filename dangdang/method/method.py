from dangdang.base.base import BasePre


class AppiumMethod:

    def __init__(self):
        global driver
        driver = BasePre().get_driver()

    @staticmethod  #写不写成静态都可以，反正测试用例中是用实例调用的
    def click_by_id(value):
        driver.find_element_by_id(value).click()

    @staticmethod
    def click(by,value):
        driver.find_element(by,value).click()
