class A:
    def fun(self):
        print('In A')


class B:
    def fun(self):
        print('In B')


class C(A,B):
    def fun(self):
        print('In C')


obj = C()
obj.fun()
