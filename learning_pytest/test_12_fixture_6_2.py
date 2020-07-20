
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
    @pytest.mark.skip
    @pytest.mark.parametrize("search_key",["python","pytest"])
    def test_search2_1(self,driver,search_key,url):
        # driver.get("http://www.baidu.com")
        driver.get(url)   # 使用conftest.py中的url
        driver.find_element_by_id("kw").send_keys(search_key)
        sleep(2)
        driver.find_element_by_id("su").click()

    def test_test(self,url):  # 验证conftest.py中的url是否正常获取
        print(url)

    if __name__=="__main__":
        pytest.main(["-s","-v","test_12_fixture_6_2.py"])

# 以上变更：搜索词参数化
