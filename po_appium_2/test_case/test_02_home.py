from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from po_appium_2.page_object.home_page import HomePage
from po_appium_2.page_object.settings_page import SettingsPage
from po_appium_2.base.base_page import BasePage
import pytest
import random

from po_appium_1.base.log import Log
from pathlib import Path

logger = Log(Path(__file__).name).get_logger()


class TestHomePage(object):

    def test_home_01_my_bar(self,driver):
        logger.info("---测试我的个人主页---")
        home=HomePage(driver, logger)
        settings=SettingsPage(driver, logger)
        if settings.is_login():   # 个人主页测试需要先登录
            home.my_home_enter()
            home.my_bar()




# if __name__=='__main__':
#     pytest.main("-s -v --html=./report/report.html test_02_home.py")







