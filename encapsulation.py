
class Student:
    _pnr = int(input("Enter PNR No :"))
    __adhar = int(input("Enter Adhar No :"))

    def detail(self):
        print("Entered PNR :",self._pnr)
        print("Entered Adhar No :",self.__adhar)

class show(Student):
    def display(self):
        print("*******************")
        print("PNR :",self._pnr)
        # print("Adhar No :",self.__adhar)          // can not access outside class 
S = Student()
D = show()
S.detail()
D.display()
