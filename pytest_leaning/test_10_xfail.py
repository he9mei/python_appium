'''
学习目标：熟悉pyetest中标记失败方法
语法：
@pytest.mark.xfail(condition,reason="string")
---condition 标记失败的条件，条件为真时，标记失败
---reason 标记失败的原因
分析：
预期失败---结果成功
预期失败---结果失败
预期成功---结果成功
预期成功---结果失败
个人理解：我的理解与老师讲的不同，
我理解的是条件为真，则标记失败；条件为假时，就不会标记。没有预期成功这个概念。
以下例子也证明我的理解貌似没有问题。
更深层的应用，待学完pytest基础知识之后，请参考：
https://www.jianshu.com/p/19441ee08410

问题：
标记失败了，实际却成功的情况，并不是我们想看到的。标记失败了，就应该是失败的。
目前显然没有达到效果，怎么控制呢？
在pytest.ini文件中添加  xfail_strict=true
'''

import pytest

class TestXfail:
    @pytest.mark.xfail(2>1,reason="条件为真，标记失败")
    def test_01(self):
        print("标记失败---结果是成功")
        assert 1

    @pytest.mark.xfail(2>1, reason="条件为真，标记失败")
    def test_02(self):
        print("标记失败---结果是失败")
        assert 0

    @pytest.mark.xfail(2<1,reason="条件为假，不会标记失败")
    def test_03(self):
        print("不会标记失败---结果是成功")
        assert 1

    @pytest.mark.xfail(2<1, reason="条件为假，不会标记失败")
    def test_04(self):
        print("不会标记失败---结果是失败")
        assert 0

'''
以上实例执行结果：
pytest_leaning/test_10_xfail.py::TestXfail::test_01 标记失败---结果是成功
XPASS
pytest_leaning/test_10_xfail.py::TestXfail::test_02 标记失败---结果是失败
XFAIL
pytest_leaning/test_10_xfail.py::TestXfail::test_03 不会标记失败---结果是成功
PASSED
pytest_leaning/test_10_xfail.py::TestXfail::test_04 不会标记失败---结果是失败
FAILED


添加 xfail_strict=true 到配置之后的执行结果是：
pytest_leaning/test_10_xfail.py::TestXfail::test_01 标记失败---结果是成功
FAILED
pytest_leaning/test_10_xfail.py::TestXfail::test_02 标记失败---结果是失败
XFAIL
pytest_leaning/test_10_xfail.py::TestXfail::test_03 不会标记失败---结果是成功
PASSED
pytest_leaning/test_10_xfail.py::TestXfail::test_04 不会标记失败---结果是失败
FAILED

'''