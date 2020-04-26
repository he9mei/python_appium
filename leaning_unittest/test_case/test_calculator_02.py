import unittest
from leaning_unittest.test_case.calculator import Calculator


class TestCalculator_02(unittest.TestCase):

    # def setUp(self):  #每个测试用例之前执行一次
    @classmethod
    def setUpClass(cls) :  #每个测试类之前执行一次
        print("测试用例之前执行")

    def test_add(self):
        c=Calculator(3,5)
        result=c.add()
        self.assertEqual(result,8)  #断言-正确
        print("测试用例-加法运算")

    def test_sub(self):
        c=Calculator(8,5)
        result=c.sub()
        # self.assertEqual(result,5)  #断言-错误
        self.assertEqual(result,3)  # 断言-正确
        print("测试用例-减法运算")

    # def tearDown(self):
    @classmethod
    def tearDownClass(cls) :
        print("测试用例之后执行")


if __name__ == "__main__":
    # unittest.main()
    # 不再用main方法，而是用TestSuit和TestRunner执行用例，
    # 好处是：1.可以灵活控制执行哪些用例，因为并不是每次都有执行所有用例；2.可以直接控制用例执行的顺序。

    #创建TestSuit
    suit=unittest.TestSuite()
    suit.addTest(TestCalculator_02("test_add"))
    suit.addTest(TestCalculator_02("test_sub"))
    #创建TestRunner
    runner=unittest.TextTestRunner()
    runner.run(suit)

# 如果存在格式问题，可能导致不会执行所有用例？
