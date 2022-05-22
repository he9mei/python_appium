#!/usr/bin/python3
# -*- coding: utf-8 -*-


import pytest

'''
-x   失败即停止
--maxfail 2  失败2个就停止   
'''


class TestDemo:
    def test_demo1(self):
        assert True

    def test_demo2(self):
        assert True

    def test_demo3(self):
        assert False

    def test_demo4(self):
        assert False

    def test_demo5(self):
        assert True


if __name__=='__main__':
    # pytest.main(['-s','-v','test_14_maxfail.py','-x'])
    pytest.main(['-s', '-v', 'test_14_maxfail.py', '--maxfail','2'])
