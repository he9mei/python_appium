import pytest

# ids可以指定用例的名称,如果不指定ids也可以，代替用例名称的位置会显示参数


class TestPara:
    @pytest.mark.parametrize("mobile,password",
                             [("18500000000","111111"),("18500228275","123456")],
                             ids=["case1_0000","case2_8275"])
    def test_login(self,mobile,password):
        print(f"账号是{mobile}密码是{password}")

    if __name__ == "__main__":
        pytest.main(["-s","-v","test_11_parametrize_ids.py"])
        # 借此用例执行junit-xml报告和session-log报告
        # pytest.main(["-s", "-v", "test_11_parametrize_ids.py","--junit-xml=./report/junit-xml.xml"])
        # pytest.main(["-s", "-v", "test_11_parametrize_ids.py","--pastebin=all"])  # certificate verify failed

'''
指定ids
test_11_parametrize_ids.py::TestPara::test_login[case1_0000] 账号是18500000000密码是111111
test_11_parametrize_ids.py::TestPara::test_login[case2_8275] 账号是18500228275密码是123456

不指定ids
test_11_parametrize_ids.py::TestPara::test_login[18500000000-111111] 账号是18500000000密码是111111
test_11_parametrize_ids.py::TestPara::test_login[18500228275-123456] 账号是18500228275密码是123456

'''