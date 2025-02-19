class A:
    def fun1(self):
        print("fun1 in A")
class B(A):
    def fun2(self):
        print("fun2 in B")
class C(B):
    def fun3(self):
        print("fun3 in C")

obj = C()

obj.fun1()
obj.fun2()
obj.fun3()