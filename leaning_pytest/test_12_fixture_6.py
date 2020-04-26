'''
scope=session实现driver全局化
结合conftest.py文件执行
结合test_12_fixture_6_2.py文件执行
'''
import pytest
from time import sleep

# @pytest.mark.usefixtures("driver")
# #这种方式是拿不到返回值的，此处并不适用；因此需要返回值时，用autouse的方式，也不适用。
class TestBaiduSearch:
    def test_search_1(self,driver):
        # driver=get_driver  #直接把conftest.py中的get_driver方法，改成了driver，则无需再赋值，问题：会不会造成混淆？
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("selenium")
        sleep(2)
        driver.find_element_by_id("su").click()

    def test_search_2(self,driver):
        # driver=get_driver
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("appium")
        sleep(2)
        driver.find_element_by_id("su").click()
'''
    @pytest.mark.usefixtures("driver")  #usefixtures的调用形式，无法拿到返回值。
    def test_search_2(self):  #即使fixture写了autouse，如果不主动传参，还是无法拿到返回值。
        # driver=get_driver
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("appium")
        sleep(2)
        driver.find_element_by_id("su").click()
'''
    # if __name__=="__main__":
    #     pytest.main("-s -v test_12_fixture_6.py")
