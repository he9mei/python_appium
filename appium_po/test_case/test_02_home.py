from selenium.webdriver.common.by import By

from appium_po.page_object.home_page import Home
from appium_po.base.base_page import Base
import pytest

class TestHomePage(object):
    def test_my_home(self,driver,logger):
        logger.info("---测试我的个人主页---")
        home=Home(driver,logger)
        home.my_home_enter()
        home.my_publish()

if __name__=='__main__':
    pytest.main("-s -v test_02_home.py")







