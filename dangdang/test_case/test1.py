# s=None
class A:
    s=None
    def test(self):
        global s
        s=2
        self.s=3
        # print(s)
        # print(self.s)

class B(A):
    def fun(self):
        # print(s)
        # self.test()
        print(s)
        print(self.s)

        A().test()
        B().fun()