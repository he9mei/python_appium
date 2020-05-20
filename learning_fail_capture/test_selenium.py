# coding=utf-8
import pytest


class TestFailScreenShoot(object):

    def test_run001(self):
        assert 1 == 2

    def test_run002(self):
        assert 1 == 1

    def test_screenshot_on_test_failure(self, browser):
        browser.get("https://www.baidu.com")
        browser.implicitly_wait(10)
        # assert False


if __name__ == "__main__":
    pytest.main('-s -v --alluredir=./report/allure_results')

