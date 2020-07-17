'''
七、pytest-fixtue
1.fixture优势
fixture相对于setup和teardown来说应该有以下几点优势：
（1）命名方式灵活，不局限于setup和teardown这几个命名。
（2）conftest.py配置里可以实现数据共享，不需要import就能自动找到一些配置。
（3）scope="module"可以实现多个.py跨文件共享前置，每一个.py文件调用一次。
（4）scope="session"可以实现多个.py跨文件使用一个session来完成多个用例。
使用：
fixture(scope="function",params=None,autouse=false,ids=None,name=None)
  使用装饰器标记fixture的功能
  可以使用此装饰器（带或不带参数）来定义fixture功能，fixture功能的名称可以在以后使用。
  引用它会在测试之前调用它：test模块或类可以使用pytest.mark.usefixtures(fixture名称)
  测试功能可以直接使用fixture名称作为输入参数。
参数：
  scope 有四个参数级别：function(默认)、class、module、session
  params 一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它。
  autouse 如果为true，则所有测试激活fixture；如果为false，则需要显示激活。
  ids 每个字符串ID的列表，没有字符串对应与params；如果没有提供ID，它们将从params自动生成。
  name fixture的名称。默认为装饰函数的名称。如果fixture在定义它的同一个模块中使用，夹具的功能名称将被请求夹具的功能arg遮蔽。
  解决这个问题的一种方法就是将装饰函数命名。"fixture_(fixturename)"然后使用@pytest.fixture(name='(fixturename)')---不太懂

2.fixture创建和使用
fixture创建：
(1) @pytest.fixture()
(2) 编写一个普通函数
@pytest.fixture()
def login()
    print("执行登录")

fixture使用：
在需要使用fixture的测试用例中，当作参数传入即可
def test_shoping(login):
    print("测试购物")

实例：使用fixture实现setup和teardown
见test_12.py
'''