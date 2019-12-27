'''
参考：
https://www.cnblogs.com/bugbreak/p/12085045.html
https://blog.csdn.net/teamo_mc/article/details/83177101
https://www.cnblogs.com/Mushishi_xu/p/7794706.html
https://blog.csdn.net/fox990152806/article/details/80197021

自己总结的3种在python中配置log的方式：
#log配置有三种方法
1.将配置写在log.conf配置文件，然后再读取配置返回logger。此处是写入fixture，用例直接将其传入。---未实现写入不同的文件名
2.将配置写在代码中，然后再调用。好处是可以自己定义文件名，方便不同的类或者方法中的log写入不同文件。
3.将配置写在py文件中，使用logging.basicConfig设置配置，传入level、filename、format等，不传入filename就会控制台输出。

'''