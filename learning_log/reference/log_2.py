# python日志
# coding=utf-8
import logging
import time
import socket
import os
import traceback

# import setting

rq = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

setting = {
    'logpath': 'D:\\logs\\',
    'filename': 'fox_' + rq + '.log'
}


# localIP = socket.gethostbyname(socket.gethostname())

class Log(object):
    def __init__(self, logger):
        self.path = setting['logpath']
        self.filename = setting['filename']
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s')
        # self.logger = logging.getLogger(logging.basicConfig(level=logging.NOTSET))
        self.logger = logging.getLogger(logger)
        self.loggerName = logger
        self.name = socket.gethostbyname(socket.gethostname())  # 获取主机名称和IP
        ###########################################################################
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        # self.logger.setLevel(logging.basicConfig(level=logging.NOTSET))
        # self.fh = logging.FileHandler(self.path + self.filename)
        ###########################################################################
        self.fh = logging.FileHandler(self.path + self.filename)
        # self.fh.setLevel(logging.DEBUG)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        ###############
        # self.fh.setLevel(logging.DEBUG)
        # self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s')
        # self.fh.setFormatter(self.formatter)
        # self.logger.addHandler(self.fh)

    def close(self):
        if rq != self.fileHandlerName:
            ################
            if self.fileHandler != None:
                self.logger.removeHandler(self.fileHandler)
                ##################
                # self.logger.addHandler(self.fh)
                # self.logger.addHandler(fh)
                self.logger.removeHandler(self.fh)

    ##############################################################################################################

    def _fmtInfo(self, msg):
        if len(msg) == 0:
            msg = traceback.format_exc()
            return msg
        else:
            _tmp = [msg[0]]
            _tmp.append(traceback.format_exc())
            return '\n**********\n'.join(_tmp)

    ###################################################################################3###########################

    # def notset(self, msg):
    #     self.logger.notset(msg)

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

    # def close(self):
    #     self.logger.addHandler(self.fh)
    #     self.logger.removeHandler(self.fh)

if __name__ == "__main__":
    logger = Log("info")
    logger.info(msg='warning')

