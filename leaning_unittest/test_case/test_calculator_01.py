import unittest
from leaning_unittest.test_case.calculator import Calculator


class TestCalculator_01(unittest.TestCase):

    def test_add(self):
        c=Calculator(3,5)
        result=c.add()
        self.assertEqual(result,8)  #断言-正确

    def test_sub(self):
        c=Calculator(8,5)
        result=c.sub()
        # self.assertEqual(result,5)  #断言-错误
        self.assertEqual(result,3)  # 断言-正确


if __name__ == "__main__":
    unittest.main()

# 如果存在格式问题，可能导致不会执行所有用例？
