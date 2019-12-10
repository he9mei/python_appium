# from dangdang.base.base1 import BasePre

'''
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

from dangdang.base.base2 import BasePre

driver = BasePre.get_driver()
class AppiumMethod:
    @staticmethod
    def click_by_id(value):
        driver.find_element_by_id(value)

    def click(self,by,value):
        driver.find_element(by,value).click()