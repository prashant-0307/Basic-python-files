from threading import Thread
from time import sleep

class A(Thread):
    def fun(self):
        for i in range(5):
            print("hello")
            sleep(1)


class B(Thread):
    def fun(self):
        for i in range(5):
            print("world")
            sleep(1)

t1 = A()
t2 = B()

t1.start()
t2.start()