from dangdang.base.base_try_3 import BasePre

# from dangdang.base.base2 import GetDriver

'''
#问题：采用继承的方式，拿到的driver值不对
class AppiumMethod(BasePre):
# class AppiumMethod:
#     @staticmethod
    def click_by_id(self,value):
        # driver=self.driver
        driver=self.get_driver()
        driver.find_element_by_id(value)
    # @staticmethod
    def click(self,by,value):
        driver=self.driver
        driver.find_element(by,value).click()
'''


class AppiumMethod:

    def __init__(self):
        global driver
        driver = BasePre().get_driver()

    # driver = BasePre().get_driver()

    # 方法传入driver的方式也可以，但是在写脚本的过程中，无法自动识别driver相关的内容
    # @staticmethod
    # def click_by_id(driver,value):
    #     driver.find_element_by_id(value).click()
    @staticmethod
    def click_by_id(value):
        # driver = GetDriver().get_driver()
        # driver=BasePre().get_driver()
        driver.find_element_by_id(value).click()

    # def click(self,by,value):
    #     driver.find_element(by,value).click()
