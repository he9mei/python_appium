
'''
scope=session实现driver全局化
结合conftest.py文件执行
结合test_12_fixture_6.py文件执行

执行时，将两个py文件一起执行，来验证scope=session的作用：跨py文件,只执行一次
pytest -s -v test_12_fixture_6.py test_12_fixture_6_2.py
'''

import pytest
from time import sleep

class TestBaiduSearch2:
    def test_search2_1(self,driver):
        # driver=get_driver
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("python")
        sleep(2)
        driver.find_element_by_id("su").click()

    def test_search2_2(self,driver):
        # driver=get_driver
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("pytest")
        sleep(2)
        driver.find_element_by_id("su").click()

    # if __name__=="__main__":
    #     pytest.main("-s -v test_12_fixture_6_2.py")cd


