# python日志
# coding=utf-8
import logging
import sys
import time

rq = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))


class Log(object):
    def __init__(self, case_name):
        self.path = "/Users/hehuaimei/PycharmProjects/python_appium/appium_po/test_result/log/"
        self.filename = case_name+"_"+rq+".log"
        # self.filename = case_name + ".log"
        self.formatter = logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-[line:%(lineno)d]-%(message)s')

        self.logger = logging.getLogger()   #不传参数，默认用root
        # self.logger.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.INFO)

        self.fh = logging.FileHandler(self.path + self.filename,"a")
        # self.fh.setLevel(logging.DEBUG)
        self.fh.setLevel(logging.INFO)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

        self.ch=logging.StreamHandler(sys.stdout,)
        # self.fh.setLevel(logging.DEBUG)
        self.ch.setLevel(logging.INFO)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)

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


