
'''
scope=session实现driver全局化
结合conftest.py文件执行
结合test_12_fixture_6.py文件执行

执行时，将两个py文件一起执行，来验证scope=session的作用：跨py文件,只执行一次
pytest -s -v test_12_fixture_6_1.py test_12_fixture_6_2.py
'''

import pytest
from time import sleep

class TestBaiduSearch2:
    @pytest.mark.parametrize("search_key",["python","pytest"])
    def test_search2_1(self,driver,search_key):
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys(search_key)
        sleep(2)
        driver.find_element_by_id("su").click()

    if __name__=="__main__":
        pytest.main("-s","-v","test_12_fixture_6_2.py")


