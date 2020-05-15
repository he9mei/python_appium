import logging
import logging.config

class Log(object):
    def __init__(self):
        self.CONF_LOG = "../log_notUseNow.conf"
        logging.config.fileConfig(self.CONF_LOG)
        self.logger = logging.getLogger()
        return self.logger