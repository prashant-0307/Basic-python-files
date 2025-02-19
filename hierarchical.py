class A:
    def fun1(self):
        print("class in A")
class B(A):
    def fun2(self):
        print("class in B")
class C(A):
    def fun3(self):
        print("class in C")

obj = B()
obj1 = C()

obj.fun1()
obj.fun2()
obj1.fun3()