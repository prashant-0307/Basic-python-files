
class A:
    def fun(self):
        print("this is class A")

class B(A):
    def fun(self):
        super().fun()
        print("this is class B")

obj = B()
obj.fun()