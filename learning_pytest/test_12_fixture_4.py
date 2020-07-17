'''
三、带返回值的fixture、fixture参数化
'''
import pytest


@pytest.fixture(params=['18500228275','18500000001'])
def phone(request):
    return request.param

'''
#这样写，会组合4次,不会对应
@pytest.fixture(params=['123456','112233'])  
def login(phone,request):
    return (phone,request.param)
'''

@pytest.fixture(params=[('18500228275','123456'),('18500000001','112233')])
def login(request):
    return request.param

def test_phone(phone):
    print(f"电话号码是：{phone}")

def test_login(login):
    print(f"登录信息是：{login}")

if __name__=="__main__":
    pytest.main(["-s","-v","test_12_fixture_4.py"])