from dangdang.test_case.test1 import A

# s=None
class C(A):
    def fun(self):
        A.test(self)
        print(self.s)
        # print(A.s)
        # print(s)



C().fun()
