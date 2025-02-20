from abc import ABC,abstractmethod

class A(ABC):
    
    @abstractmethod
    def input(self):
        pass
    @abstractmethod
    def output(self):
        pass

class B(A):
    a = 10
    def input(self):
        a = int(input("Enter no :"))

    def output(self):
        print("no :",self.a)

obj = B()

obj.input()
obj.output()