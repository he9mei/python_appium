import logging


logging.basicConfig(level=logging.INFO,filename="runlog.log",format="%(asctime)s%(filename)s [line:%(lineno)d] %(levelname)s %(message)s")
# logging.basicConfig(level=logging.INFO,format="%(asctime)s%(filename)s [line:%(lineno)d] %(levelname)s %(message)s")
#写了filename就写在文件中，不写filename就打印在控制台

def test_log():
    logging.info("日志测试信息")

if __name__=="__main__":
    test_log()