import logging
import time
import os.path
import sys

class LogDemo:
    def log(self,class_name="Test",func_name="test"):
        now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        path="./log/"+class_name+"_"+now  #如果文件路径不存在，需要先创建
        # filepath=os.path.dirname(os.getcwd())+"/log"  #python_appium/learning_log/log
        if not os.path.exists(path):
            os.makedirs(path)

        logger=logging.getLogger("logger")
        logger.setLevel(logging.DEBUG)

        sh=logging.StreamHandler()
        fh=logging.FileHandler(filename="{}/{}_{}.log".format(path,func_name,now),mode="a")

        formatter=logging.Formatter(fmt="%(asctime)s-[%(filename)s-%(funcName)s]-%(levelname)s-[line:%(lineno)d]-%(message)s",
                                   datefmt="%Y/%m/%d/%X")

        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(sh)
        logger.addHandler(fh)

        # logger.debug("debug信息")
        # logger.info("info信息")
        # logger.warning("warning信息")
        # logger.error("error信息")
        # logger.critical("critical信息")

        return logger


    def sum(self,a,b):
        sum=a+b
        class_name=self.__class__.__name__
        func_name=sys._getframe().f_code.co_name
        logger=self.log(class_name,func_name)
        logger.info("{}+{}的值是{}".format(a,b,sum))


# LogDemo().log("test")
logdemo=LogDemo()
logdemo.sum(2,3)
logdemo.sum(4,5)

'''
#存在问题：
1.如果path不存在，则无法保存log---解决办法：先判断，如果不存在则新建路径
        if not os.path.exists(path):
            os.makedirs(path)
            
2.多次调用时，会重现重复数据---解决办法：需要加是否存在handler的判断
2020/05/11/19:38:25-[log.py-sum]-INFO-[line:43]-2+3的值是5
2020/05/11/19:38:25-[log.py-sum]-INFO-[line:43]-4+5的值是9
2020/05/11/19:38:25-[log.py-sum]-INFO-[line:43]-4+5的值是9
'''





