# python日志
# coding=utf-8
import logging
import sys
import time
import socket
import os
import traceback


rq=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))

class Log(object):
    def __init__(self, case_name):
        self.path = "/Users/hehuaimei/PycharmProjects/python_appium/po_appium_1/test_result/log/"
        self.filename = case_name+"_"+rq+".log"
        self.formatter = logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-[line:%(lineno)d]-%(message)s')

        self.logger = logging.getLogger()   #不传参数，默认用root
        self.logger.setLevel(logging.DEBUG)

        self.fh = logging.FileHandler(self.path + self.filename,"a")
        self.fh.setLevel(logging.DEBUG)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

        self.ch=logging.StreamHandler(sys.stdout,)
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)

#暂未实践该方法
    def close(self):
        if rq != self.fileHandlerName:
            if self.fileHandler != None:
                self.logger.removeHandler(self.fileHandler)
                self.logger.removeHandler(self.fh)

#暂未实践该方法
    def _fmtInfo(self, msg):
        if len(msg) == 0:
            msg = traceback.format_exc()
            return msg
        else:
            _tmp = [msg[0]]
            _tmp.append(traceback.format_exc())
            return '\n**********\n'.join(_tmp)

    def notset(self, msg):
        self.logger.notset(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == "__main__":
    logger = Log("just_test")
    logger.info('---测试一下，哎呀呀---')

