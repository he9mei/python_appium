from dangdang.pages.login_page import ElementLogin
class TestCase:
    def test_01(self):
        print("第1个用例")
    def test_02(self):
        el="com.dangdang.reader:id/tab_personal_iv"
        # el=ElementLogin.id_tab_personal
        print(el)
