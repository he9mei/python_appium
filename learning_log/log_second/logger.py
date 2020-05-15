import logging
import time
import os.path
import sys

class Logger:
    def logger(self,py_name="test.py"):
        '''
        class_name="Test"
        func_name="test"
        class_name和func_name获取稍微麻烦点，换成直接使用py_name
        '''
        now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        path="./log"  #如果文件路径不存在，需要先创建
        # path = "./log/" + class_name + "_" + now #一个class的log文件放入一个文件夹
        # filepath=os.path.dirname(os.getcwd())+"/log"  #python_appium/learning_log/log
        if not os.path.exists(path):
            os.makedirs(path)

        #创建日志器
        logger=logging.getLogger("logger")
        logger.setLevel(logging.DEBUG)

        #判断是否已经存在处理器
        if not logger.handlers:
            #创建处理器
            sh=logging.StreamHandler()
            fh=logging.FileHandler(filename="{}/{}_{}.log".format(path,py_name,now),mode="a")  #py_name换掉func_name
            #创建个格式器
            formatter=logging.Formatter(fmt="%(asctime)s-[%(filename)s-%(funcName)s]-%(levelname)s-[line:%(lineno)d]-%(message)s",
                                       datefmt="%Y/%m/%d/%X")

            sh.setFormatter(formatter)
            fh.setFormatter(formatter)

            logger.addHandler(sh)
            logger.addHandler(fh)

        return logger





