'''
from pytest付费课程
六、pytest高阶用法

1、跳过测试函数
根据特定的条件，不执行标识的测试函数
方法：skipif(condition,reason=None)
参数：condition表示跳过的条件，必传参数；reason表示跳过的原因，比传参数
使用方法：
在需要跳过的测试函数前，添加
@pytest.mark.skipif(condition,reason=None)
实例见test_09.py
对比：如果直接用 @pytest.mark.skip 则不需要条件，直接跳过

2.标记为失败
方法：xfail(condition=None,reason=None,raises=None,run=True,strict=False)
常用参数：
condition：预期失败的条件，必传参数
reason：预期失败的原因，必传参数
使用方法：
在测试函数前添加：
@pytest.mark.xfail(condition,reason="string")
实例见test_10.py
目前的例子不能体现其价值，待pytest学完之后来看一个更实际的例子：
https://www.jianshu.com/p/19441ee08410
问题：
标记失败了，实际却成功的情况，并不是我们想看到的。标记失败了，就应该是失败的。
目前显然没有达到效果，怎么控制呢？
在pytest.ini文件中添加  xfail_strict=true

3.函数数据参数化
方便测试函数对测试数据的获取。
方法：
parametrize(argnames,argvalues,indirect=False,ids=None,scope=None)
常用参数：
argnames 参数名
    一个参数时，"参数名"
    多个参数时，"参数1-名，参数2-名"
argvalues  参数值，类型为list
    一个参数时，["参数值1"，"参数值2"，"参数值3"]
    多个参数时，[("参数1-值1"，"参数2-值1"),("参数1-值2"，"参数2-值2"),("参数1-值3"，"参数2-值3")]
使用方法：
在测试函数前添加：
@pytest.mark.parametrize(argnames,argvalues)
有多少个参数值，就会执行多少次
实例见test_11.py
'''

