'''
一、测试用例执行顺序
（1）创建测试套件，主动加入测试用例，即可确定了测试用例执行的顺序。
（2）main()方法和discover()方法，都是使用的unittest默认顺序，是按照ASCII码的顺序加载测试用例的。
（数字与字母的顺序为0-9,a-z,A-Z），并不是按照测试用例从上到下顺序执行的。所以需要在测试用例的命名上可以加以控制。
总结：测试套件的方式，如果测试用例很多时，添加比较麻烦；最好的办法还是通过命名控制执行顺序。

二、执行多级目录测试用例
如果将discover()方法中的start_dir定义为"./test_case"，只能找到该目录下的用例，
而"./test_case/"子目录下的用例是找不到的。如果想让它找到，则需要在每一个子目录下放一个__init__.py文件。
__init__.py文件的作用是将一个目录标记为一个标准的python模块。
备注：经过验证，如果子目录有__init__.py文件，确实可以找到；如果删除，则找不到。

三、跳过测试和预期失败
unittest.skip(reason)  无条件跳过
unittest.skipIf(condition,reason)  条件为真，跳过测试
unittest.skipUnless(condition,reason) 条件为真，执行测试
unittest.expectedFailure()  不管执行结果是否失败，都将标记为失败。

四、fixture
setUp/tearDown  作用范围：方法级别
setUpClass/tearDownClass 作用范围：类级别，需要通过@classmethod修饰，参数为cls，实际与self没有什么区别
setUpModule/tearDownModule 作用范围：模块级别，在整个py文件的开始和结束执行

其他问题总结：
1.是否要把断言写在封装的方法中？
个人建议还是把断言写在每一个测试用例中比较清晰，而且即使步骤相同，断言内容也不一定相同。
2.setUpClass/tearDownClass，使用cls.driver，但是在其他地方使用时仍然可以用self.driver

'''