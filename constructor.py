
# ------------------Default constructor-----------------
# class A:
#     age = 20

#     def __init__(self):
#         print("default constructor :",self.age)

# obj = A()

# -----------------Parameterized Constructor--------------

class A:
    age = 20
    def __init__(self,rollno):
        print("Parameterized Constructor :",self.age,rollno)

obj = A(30)