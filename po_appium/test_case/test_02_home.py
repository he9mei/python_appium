from selenium.webdriver.common.by import By

from po_appium.page_object.home_page import Home
from po_appium.base.base_page import Base
import pytest
import random

from po_appium.page_object.personal_page import Personal


class TestHomePage(object):
    def test_my_home(self,driver,logger):
        logger.info("---测试我的个人主页---")
        home=Home(driver,logger)
        home.my_home_enter()
        home.my_bar()


if __name__=='__main__':
    pytest.main("-s -v --html=./report/report.html test_02_home.py")







