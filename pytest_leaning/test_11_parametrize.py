
'''
学习目标：必须掌握pytest参数化使用方法
语法：
@pytest.mark.parametrize(argnames,argvalues)
---argnames 参数名
---argvalues 参数值 类型为list
场景：
1个参数的情况
"参数名"，["参数值1","参数值2"...]
多个参数，且相互对应的情况，如一个账号名对应一个密码
"参数名1，参数名2"，[("参数值1-1","参数值2-1"),("参数值1-2","参数值2-2")...]
注意：参数名和参数值都需要引号
'''

import pytest


class TestPara:
    @pytest.mark.parametrize('mobile', ["18500228275", "1850000001", "18500000002"])
    # @pytest.mark.parametrize('password', ["123456", "111111", "222222"])  #这样写两个参数化，3个参数值会相互匹配3*3=9次，不会相互对应
    def test_register(self,mobile):
        # print("注册手机号{}".format(mobile))
        print(f"注册手机号{mobile}")  #格式化输出新学到的用法

    @pytest.mark.parametrize("mobile,password", [("18500228275","123456"), ("18500000001","111111"), ("18500000002","222222")])
    def test_login(self,mobile,password):
        print(f"登录的手机号是{mobile}密码是{password}")

'''
执行结果：
pytest_leaning/test_11_parametrize.py::TestPara::test_register[18500228275] 注册手机号18500228275
PASSED
pytest_leaning/test_11_parametrize.py::TestPara::test_register[1850000001] 注册手机号1850000001
PASSED
pytest_leaning/test_11_parametrize.py::TestPara::test_register[18500000002] 注册手机号18500000002
PASSED
pytest_leaning/test_11_parametrize.py::TestPara::test_login[18500228275-123456] 登录的手机号是18500228275密码是123456
PASSED
pytest_leaning/test_11_parametrize.py::TestPara::test_login[18500000001-111111] 登录的手机号是18500000001密码是111111
PASSED
pytest_leaning/test_11_parametrize.py::TestPara::test_login[18500000002-222222] 登录的手机号是18500000002密码是222222
PASSED

'''