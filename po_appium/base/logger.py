import logging
import time
import os.path
import sys

class Logger:
    # 也可以把获得logger的方法写在init方法中，实例化时就会调用
    def logger(self,py_name="test.py"):
        '''
        class_name="Test"
        func_name="test"
        class_name和func_name获取稍微麻烦点，换成直接使用py_name
        '''
        now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
        path="./test_result/log"  #如果文件路径不存在，需要先创建
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
            # sh=logging.StreamHandler(sys.stdout, )
            py_name_str = py_name.split(".py")[0]  #拿到py_name再以".py"分隔，取前面的字符串（不切割也能正常生成log）
            fh=logging.FileHandler(filename="{}/{}_{}.log".format(path, py_name_str, now), mode="a", encoding="utf-8")  #py_name换掉func_name
            #注意：此处需要加上encoding="utf-8"，否则Windows上生成的log文件显示问号，打不开。
            #创建个格式器
            formatter = logging.Formatter(fmt="%(asctime)s-[%(filename)s-%(funcName)s]-%(levelname)s-[line:%(lineno)d]-%(message)s",
                                       datefmt="%Y/%m/%d/%X")

            sh.setFormatter(formatter)
            fh.setFormatter(formatter)

            # sh.setLevel(logging.DEBUG)
            # fh.setLevel(logging.INFO)

            logger.addHandler(sh)
            logger.addHandler(fh)

        return logger

'''
# 我这里用到的python日志2种方式：
# 1.封装获得logger的方法，用的时候实例化，调用方法获得logger；（可以传参数）
# 2.用log.conf配置文件，文件的解析写在conftest.py中了，加上fixture装饰器，使用时直接当成参数传入。
（fixture的方式，目前不知道怎么传入参数）
还有一种py文件内的BasicConfig配置方式，用的比较少。
'''



