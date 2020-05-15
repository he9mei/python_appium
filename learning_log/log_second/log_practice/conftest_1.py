import logging
import time
import os.path
import pytest

@pytest.fixture(scope="session")
def logger():
    # class_name = self.__class__.__name__
    # func_name = sys._getframe().f_code.co_name
    # class_name="Test"
    func_name="test"

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
        fh=logging.FileHandler(filename="{}/{}_{}.log".format(path,func_name,now),mode="a")
        #创建个格式器
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


'''
尝试：
如果直接使用conftest.py的logger,可以;
但是无法传入class_name/func_name/py_name参数，所有的log在一起。

'''



