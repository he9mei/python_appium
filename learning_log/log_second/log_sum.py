from learning_log.log_second.log import LogDemo
import sys


class LogSum:

    '''
    def func_sum(self,a,b,class_name):  #方法外部用实例传入class_name
        case_name = sys._getframe().f_code.co_name
        logger=LogDemo().log(class_name,case_name)
        sum=a+b
        logger.info("{}+{}的值是{}".format(a, b, sum))
    '''

    def func_sum(self, a, b):  #方法内用self获取class_name
        self.class_name=self.__class__.__name__
        self.func_name = sys._getframe().f_code.co_name
        #每个用例都要赋值case_name还是很麻烦
        logger=LogDemo().log(self.class_name,self.func_name)
        sum=a+b
        logger.info("{}+{}的值是{}".format(a, b, sum))

ts=LogSum()
# class_name=ts.__class__.__name__
# ts.func_sum(5,6,class_name)
#实例化之后再获得class_name，太麻烦了；可以直接在方法内用self获取
ts.func_sum(5,6)

#能实现每一个class的log文件放在一个文件夹，每一个function的log放在一个文件
#但是每个用例都要赋值class_name和case_name还是很麻烦
'''
获取class名就是 xx.__class__.__name__    其中xx是class实例；或者用self获取
获取调用方法名：sys._getframe().f_code.co_name  不要忘了引用sys模块
'''