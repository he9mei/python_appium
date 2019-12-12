'''
掌握pytest中失败用例重跑机制
安装：pip3 install pytest-rerunfailues
使用：增加命令  --reruns=2  即重跑2次
总结：用例重跑的时候，如果重跑次数内就通过了，剩下的次数不用再执行
'''

class TestRerun:
    def test_1(self):
        print("第1个测试用例")
        assert 1

    def test_2(self):
        print("第2个测试用例")
        assert 0