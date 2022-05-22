
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

login_data_tupe=[("18500228275","123456"),
            ("18500000001","111111"),
            ("18500000002","222222")]

login_data_dict=[{"account":"18500228275","pw":"12345"},
                 {"account":"18500000001","pw":"111111"},
                 {"account":"18500000002","pw":"222222"}]

class TestPara:
    '''
    @pytest.mark.parametrize('mobile', ["18500228275", "1850000001", "18500000002"])
    # @pytest.mark.parametrize('password', ["123456", "111111", "222222"])  #这样写两个参数化，3个参数值会相互匹配3*3=9次，不会相互对应
    def test_register(self,mobile):
        # print("注册手机号{}".format(mobile))
        print(f"注册手机号{mobile}")  #格式化输出新学到的用法

    @pytest.mark.parametrize("mobile,password", [("18500228275","123456"), ("18500000001","111111"), ("18500000002","222222")])
    def test_login1(self,mobile,password):
        print(f"登录的手机号是{mobile}密码是{password}")

    #尝试把数据单独写出来
    #方法1：把数据写成元组组成的列表
    @pytest.mark.parametrize("data",login_data_tupe)
    def test_login2(self,data):
        print(f"登录的手机号是{data[0]}密码是{data[1]}")
    '''
    #方法2：把数据写成字典组成的列表
    '''
    @pytest.mark.parametrize("data",login_data_dict)
    def test_login3(self,data):
        # print(f"登录的手机号是{data["account"]}密码是{data["pw"]}")  #这种情况下格式化输出无法识别key
        print("登录的手机号是"+data["account"]+"密码是"+data["pw"])  #直接输入是可以的
    '''

    # 补充一种写法---类似于解包
    @pytest.mark.parametrize("account,pw", login_data_dict)
    def test_login3(self, account, pw):
        # print(f"登录的手机号是{data["account"]}密码是{data["pw"]}")  #这种情况下格式化输出无法识别key
        print("登录的手机号是" + account + "密码是" + pw)  # 直接输入是可以的

    # 方法3：把数据写在excel中---可以通过Python_api中的do_excel.py实现


'''
执行结果：
learning_pytest/test_11_parametrize.py::TestPara::test_register[18500228275] 注册手机号18500228275
PASSED
learning_pytest/test_11_parametrize.py::TestPara::test_register[1850000001] 注册手机号1850000001
PASSED
learning_pytest/test_11_parametrize.py::TestPara::test_register[18500000002] 注册手机号18500000002
PASSED
learning_pytest/test_11_parametrize.py::TestPara::test_login[18500228275-123456] 登录的手机号是18500228275密码是123456
PASSED
learning_pytest/test_11_parametrize.py::TestPara::test_login[18500000001-111111] 登录的手机号是18500000001密码是111111
PASSED
learning_pytest/test_11_parametrize.py::TestPara::test_login[18500000002-222222] 登录的手机号是18500000002密码是222222
PASSED

'''