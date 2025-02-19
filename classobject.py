# class a:
#     print("inside a class")

# obj = a()


# class A:
#     def fun(self):
#         a= 10
#         print(a)

# obj = A()

# obj.fun()

# classes
# class A:
#     def __init__(self,rollno):
#         name = "prashant"
#         age = 21
#         print(name)
#         print(age)
#         print(rollno)


# # main code
# a= int(input("enter rollno :"))
# obj = A(rollno=a)

class A:
    def fun(self):
        "this is comment"
        print("inside of fun function")

obj = A()

print(obj.fun.__doc__)
obj.fun()