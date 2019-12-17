'''
2.yield和addfinalizer
(1)yield：当用例执行完毕之后，会执行yield后面的代码，但不能return
(2)addfinalizer这个实现功能与yield一样，可以return参数，传给后面的用例
'''

#实例2

import pytest
#创建fixture
@pytest.fixture()
def driver():





# if __name__=="__main__":
#     pytest.main("-s -v test_12_fixture_2.py")