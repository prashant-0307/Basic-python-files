from abc import ABC, abstractmethod

class School:
    def detail(self):
        name = input("Enter Name :")
        print("name",name)

    @abstractmethod
    def Reg(self):
        pass

class student1(School):
    def Reg(self):
        rollno = int(input("Enter rollno :"))
        print("rollno :",rollno)

class student2(School):
    def Reg(self):
        rollno = int(input("Enter rollno :"))
        print("rollno :",rollno)

S1 = student1()
S2 = student1()

S1.detail()
S1.Reg()

S2.detail()
S2.Reg()