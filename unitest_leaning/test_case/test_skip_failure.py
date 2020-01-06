import unittest


class TestSkipAndFailure(unittest.TestCase):
    @unittest.skip("无条件跳过测试")
    def test_skip(self):
        print("测试skip")

    @unittest.skipIf(3>2,"条件为真时跳过测试")
    def test_skip_if(self):
        print("测试skipIf")

    @unittest.skipUnless(2>1,"条件为真是执行测试")
    def test_skip_unless(self):
        print("测试skipUnless")

    @unittest.expectedFailure   #预期失败
    def test_failure(self):
        self.assertEqual(2+2,5)


if __name__ == "__main__":
    unittest.main()