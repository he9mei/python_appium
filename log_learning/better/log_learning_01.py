'''
参考：
https://www.cnblogs.com/bugbreak/p/12085045.html
https://blog.csdn.net/teamo_mc/article/details/83177101
https://www.cnblogs.com/Mushishi_xu/p/7794706.html
https://blog.csdn.net/fox990152806/article/details/80197021
新增参考：https://www.cnblogs.com/xianyulouie/p/11041777.html

总结：
日志级别
debug、info、warn、error、critical五个级别

logging模块构成（四部分）
logger（记录器，用于日志采集）
Handler（处理器，将日志记录发送到合适的路径）
Filter（过滤器，提供了更好的粒度控制，决定输出哪些日志记录）
Formatter（格式化起，指明了日志的格式）

logger（记录器）
在使用debug、info、warn、error、critical五个级别之前创建logging实例

方法：basicConfig（）为日志记录系统做基础配置

# -*- coding: utf-8 -*-#
import logging
# 根据日志级别输出
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.CRITICAL)
logging.debug("debug info")
logging.info("hello world")
logging.warning("warnning info")
logging.error("error info")
logging.critical("critical info")

Handler（处理器）
1.StreamHandler
将日志记录输出发送到sys.stdout，sys.stderr货值任何类似文件流的对象，上面的例子就是输出到控制台
2.FileHandler
将日志记录输出发送到磁盘文件，继承了StreamHandler的输出功能
logging.basicConfig(filename="runlog.log",lever=logging.DEBUG)
运行后当前脚本路径会生成一个runlog.log文件，用于记录日志
3.NullHandler
不做任何格式化或输出，本质是一个开发人员使用“无操作”处理程序。

Filter（过滤器）
可以使用Filters来完成比级别更加复杂的过滤

Formatter
使用Formatter对象设置日志信息最后的规则、结构和内容，默认的时间为%Y-%m-%d %H%M%S
%(levelno)s                       打印日志级别数值
%(levelname)s                   打印日志级别名称
%(pathname)s                   打印当前执行程序路径
%(filename)s                      打印当前执行程序名称
%(funcName)s                    打印日志当前函数
%(lineno)d                          打印日志当前行号
%(asctime)s                        打印日志时间
%(thread)d                          打印线程id
%(threadName)s                 打印线程名称
%(process)s                        打印进程ID
%(message)s                       打印日志信息

方法：
logging.basicConfig(level=logging.DEBUG,filename="runlog.log",format="%(asctime)s%(filename)s[line:%(lineno)d] %(levelname)s %(message)s")


---更详细的format---
1.初始化 logger = logging.getLogger("endlesscode")，getLogger()方法后面最好加上所要日志记录的模块名字，后面的日志格式中的%(name)s 对应的是这里的模块名字
2. 设置级别 logger.setLevel(logging.DEBUG),Logging中有NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL这几种级别，日志会记录设置级别以上的日志
3. Handler，常用的是StreamHandler和FileHandler，windows下你可以简单理解为一个是console和文件日志，一个打印在CMD窗口上，一个记录在一个文件上
4. formatter，定义了最终log信息的顺序,结构和内容，我喜欢用这样的格式 '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S'，
%(name)s Logger的名字
%(levelname)s 文本形式的日志级别
%(message)s 用户输出的消息
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(levelno)s 数字形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s  调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有


---log.conf文件读取---
import logging
import logging.config
#这个是配置文件的路径
CONF_LOG = "../Config/log.conf"
logging.config.fileConfig(CONF_LOG)
logger = logging.getLogger()
#下面就是使用日志打印日志信息
logger.info("info类型的日志")
logger.error("error 的日志")


'''