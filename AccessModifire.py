class A:
    a = 10      # public
    _b = 20     # protected
    __c = 30    # private

    def fun(self):
        print(self.a," ",self._b," ",self.__c)

class B:
    def fun(self):
        print(A.a," ",A._b," ",A.__c) # error not access __c in other class

obj = A()
obj1 = B()
obj.fun()
obj1.fun()
