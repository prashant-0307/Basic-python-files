class A:
    def fun1(self):
        print("Class in A")

class B:
    def fun2(self):
        print("Class in B")

class C(A,B):
    def fun3(self):
        print("Class in C")

obj = C()

obj.fun1()
obj.fun2()
obj.fun3()