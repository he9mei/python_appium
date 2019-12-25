from appium_po.page_object.home_page import Home
from appium_po.base.base_page import Base
import pytest

class TestHomePage(object):
    def test_my_home(self,driver):
        home=Home(driver)
        base=Base(driver)
        home.my_home_enter()
        base.swipe_up(2)
        base.swipe_down(1)

if __name__=='__main__':
    pytest.main("-s -v test_02_home.py")







