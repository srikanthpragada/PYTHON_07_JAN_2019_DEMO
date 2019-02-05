
class Common(object):
    def fun(self):
        print('In Common')

class A(Common):
    def fun2(self):
        print('In A')


class B(Common):
    def fun(self):
        print('In B')

class C(A,B):
    pass
    # def fun(self):
    #     print('In C')


obj = C()
print(C.mro())

