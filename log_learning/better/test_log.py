
from log_learning.better.log_conf import Log
import pytest
import logging


class TestLog():
    # filename="TestLog"
    # logging.basicConfig(level=logging.INFO,filename="../test_result/log/" + filename + ".log",
    #                     format="%(asctime)s-%(filename)s-%(levelname)s-[line:%(lineno)d]-%(message)s")
    # 写了filename就写在文件中，不写filename就打印在控制台
    def test_log_1(self,logger):
        logger.info("----测试一下看看呢---")
        # logging.info("---可以改名呀---啦啦啦---")
        #如果传入了logger，前面的logging.basicConfig就不会生效了,没有办法结合使用

    def test_log_2(self):
        logger=Log(self.__class__.__name__)
        logger.info("---哈哈哈，测试一下吧---")

    if __name__=="__main__":
        pytest.main("-s -v test_log.py::TestLog::test_log_2")




