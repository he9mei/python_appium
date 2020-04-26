import logging
import logging.config

def test_log():
    CONF_LOG = "../log.conf"
    logging.config.fileConfig(CONF_LOG)
    logger = logging.getLogger()
    logger.info("--测试日志---")

if __name__=="__main__":
    test_log()