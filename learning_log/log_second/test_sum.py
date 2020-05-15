import pytest
from learning_log.log_second.logger import Logger
from pathlib import Path
import sys

logger = Logger().logger(py_name=Path(__file__).name)

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

    '''
    #以下使用方法内获得logger，并且传入class_name和func_name
    def test_sum_1(self):
        self.class_name = self.__class__.__name__
        self.func_name = sys._getframe().f_code.co_name
        logger = LogDemo().log(self.class_name, self.func_name)
        sum=self.func_sum(8,9)
        logger.info("求和结果是：{}".format(sum))
    
    # 以下使用conftest.py传入的logger
    # @pytest.mark.usefixtures("logger")
    def test_sum_2(self,logger):
        sum = self.func_sum(8, 9)
        logger.info("求和结果是：{}".format(sum))
        #logger无法传入参数，如class_name
        logger.info("just test")
   
    #以下使用，conftest.py初始化initlog获取当前py_name、或func_name
    # 不行---获取的是conftest.py文件名；获取的initlog的函数名
    def test_sum_3(self,initlog):
        sum = self.func_sum(8, 9)
        initlog.info("求和结果是：{}".format(sum))
        initlog.info("just test")
    '''

   #以下使用py文件内获取一次logger，并且传入py_name
    def test_sum_4(self):
        logger.info(f"---{sys._getframe().f_code.co_name}---")
        sum = self.func_sum(8, 9)
        logger.info("求和结果是：{}".format(sum))
        logger.info("just test")

if __name__=="__main__":
    pytest.main("-s -v ./test_sum.py")

'''
# if __name__=="__main__":
#     pytest.main("-s -v ./test_sum.py::TestSum::test_sum_2")
以上写法有问题，无法只定位到一个用例，py文件下的用例都会都执行；或者使用skip

或者用终端执行：
-->pytest -s -v ./test_sum.py::TestSum::test_sum_2
'''





