class A:
    def fun1(self):
        return "A"
class B(A):
    def fun2(self):
        return "B"

obj = B()

a = obj.fun1()
b = obj.fun2()

print(a)
print(b)
