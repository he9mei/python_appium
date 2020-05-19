from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from po_appium.page_object.home_page import Home
from po_appium.page_object.settings_page import Settings
from po_appium.base.base_page import Base
import pytest
import random

from po_appium.base.log import Log
from pathlib import Path

logger = Log(Path(__file__).name).get_logger()


class TestHomePage(object):

    def test_home_01_my_bar(self,driver):
        logger.info("---测试我的个人主页---")
        home=Home(driver,logger)
        settings=Settings(driver,logger)
        if settings.is_login():   # 个人主页测试需要先登录
            home.my_home_enter()
            home.my_bar()




# if __name__=='__main__':
#     pytest.main("-s -v --html=./report/report.html test_02_home.py")







