'''
一、基本用法
引入unittest模块
1.用unittest编写用例需要遵循规则：
（1）创建测试类，以Test开头，必须继承unittest.TestCase类
（2）创建测试方法，必须要以test开头
2.可以使用unittest提供的断言方法，直接以self调用，如self.assertEqual()
3.调用unittest.main()来执行用例，它会按照前面两条规则来查找并执行用例。

二、4个基本概念
unittest有4个基本概念：Test Case、Test Suit、Test Runner、Test Fixture
Test Case：最小测试单元，unittest提供了TestCase基类，我们创建的测试类需要继承该基类，用以创建新的测试用例。
Test Suit：测试套件，用于组装一组要运行的测试。unittest提供了TestSuit类来创建测试套件。
Test Runner：是一个组件，用于协调测试的执行并向用户提供结果。可以使用图形界面、文本界面或返回特殊值来展示执行的测试结果。
unittest提供了TextTestRunner类运行测试测试用例，为了生成报告，后面会选用HTMLTestRunner运行类。
Test Fixture：代表执行一个或多个测试所需的环境准备，以及关联的清理动作。
unittest提供了setUp()/tearDown()、setUpClass()/tearDownClass()等方法来完成这些操作。

三、断言
unitest框架的TestCase类提供的用于测试结果的断言的方法如下：
assertEqual(a,b)      a=b
assertNotEqual(a,b)   a!=b
assertTrue(x)         x is True
assertFalse(x)        x is False
assertIs(a,b)         a is b
assertIsNot(a,b)      a is not b
assertIsNone(x)       x is None
assertIsNotNone(x)    x is not None
assertIn(a,b)         a in b
assertNotIn(a,b)      a not in b
assertIsInstance(a,b)     isinstance(a,b)
assertNotIsInstance(a,b)  not isinstance(a,b)

四、用例的组织和发现
用例的组织建议：一个测试类对应一个被测试功能。
一个测试py文件可以定义多个测试类，只要他们遵循测试用例的规则，main()方法就能找到他们。
unittest中的TestLoader提供的discover方法可以从多个文件中查找测试用例。
unittest提供可以共享的defaultTestLoader类，可以使用其子类或方法创建实例，discover()方法就是其中之一。
discover(start_dir,pattern="test*.py",top_level_dir=None)
start_dir：待测试的模块名或者测试用例目录
pattern：测试用例文件名匹配规则
top_level_dir：测试模块的顶层目录，如果没有则默认为None

'''