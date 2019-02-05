class A():
    def fun(self):
        print('In A')


class B(A):
    def fun(self):
        print('In B')


class C(B, A):
    pass


obj = C()
print(C.mro())
