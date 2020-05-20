'''
补充：
1、scope=session的使用
 (1).fixture为session级别是可以跨.py模块调用的，也就是当我们有多个.py文件的用例的时候，
 如果多个用例只需调用一次fixture，那就可以设置为scope="session"，并且写到conftest.py文件里。
 (2).conftest.py文件名称时固定的，pytest会自动识别该文件。放到项目的根目录下就可以全局调用了，
 如果放到某个package下，那就在改package内有效。
 (3).1个工程下可以建多个conftest.py的文件，一般在工程根目录下设置的conftest文件起到全局作用。
 在不同子目录下也可以放conftest.py的文件，作用范围只能在改层级以及以下目录生效。
实例见：test_12_fixture_6

2、usefixtures与传fixture区别
 如果fixture有返回值，那么usefixture就无法获取到返回值，这个是装饰器usefixture与用例直接传fixture参数的区别。
 当fixture需要用到return出来的参数时，只能讲参数名称直接当参数传入，不需要用到return出来的参数时，两种方式都可以。

3、fixture自动使用autouse=True
当用例很多的时候，每次都传这个参数，会很麻烦。fixture里面有个参数autouse，默认是False没开启的，
可以设置为True开启自动使用fixture功能，这样用例就不用每次都去传参了
autouse设置为True，自动调用fixture功能

参考：
https://www.cnblogs.com/huizaia/p/10331469.html
'''

