class A:
    def fun1(self):
        print("class A")

class B(A):
    def fun2(self):
        print("Class B")

class C(B):
    def fun3(self):
        print("Class C")

obj = C()

obj.fun1()
obj.fun2()
obj.fun3()

