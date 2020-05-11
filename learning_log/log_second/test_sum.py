from learning_log.log_second.log import LogDemo
import sys
import pytest

class TestSum:
    def func_sum(self, a, b):
        # self.class_name=self.__class__.__name__
        # self.func_name = sys._getframe().f_code.co_name
        #写在方法函数中，取到的是这个方法函数的名字，而不是调用方法的测试用例的函数名字。
        #待改进：每个用例都要赋值func_name还是很麻烦
        # logger=LogDemo().log(class_name,func_name)
        sum=a+b
        # logger.info("{}+{}的值是{}".format(a, b, sum))
        return sum

    def test_sum(self):
        self.class_name = self.__class__.__name__
        self.func_name = sys._getframe().f_code.co_name
        logger = LogDemo().log(self.class_name, self.func_name)
        sum=self.func_sum(8,9)
        logger.info("求和结果是：{}".format(sum))

    #以下使用conftest.py传入的logger
    def test_sum_2(self,logger):
        sum = self.func_sum(8, 9)
        logger.info("求和结果是：{}".format(sum))
        #logger的两个参数没有传
        #有问题。。。。。。


if __name__=="__main__":
    pytest.main("-s -v ./test_sum_2.py")




