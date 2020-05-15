from learning_log.log_second.logger import Logger
import pytest
from pathlib import Path
import sys

'''
@pytest.fixture(scope="module",autouse=True)
def initlog():
    # func_name = sys._getframe().f_code.co_name
    py_name = Path(__file__).name
    logger = Logger().logger(py_name)
    logger.info(f"当前py文件是:{py_name}")
    return logger
'''
@pytest.fixture(scope="function",autouse=True)
def initlog():
    func_name = sys._getframe().f_code.co_name
    logger = Logger().logger(func_name)
    logger.info(f"当前function是:{func_name}")
    return logger

'''
备注：
这种方式也不行，
获取到的py文件名都是contest.py，获取不到调用的py文件;
获取到的function名是initlog，获取不到调用的函数名。

问题：fixture函数，怎么传参数呢？

'''