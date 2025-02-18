# 1) default function

# def fun():
#     print("hello world")

# fun()

# 2) parameter function with unorder

# def fun(a,b):
#     print("addition",a+b)

# fun(2,5)

# 3) parameter function with order

# def fun(firstname,lastname):
#     print("FirstName :",firstname,"\nLastName :",lastname)

# fun("prashant","gardas")

# # 4)return type function
# def fun(a,b):
#     return a+b
# a= fun(2,3)
# print("Addition :",a)

#   5) tuple type function

# def fun(*args):
#     print(args)
#     print(type(args))

# fun(1,2,3,4,5)


#  6) dict type function


def fun(**args):
    print(args)
    print(type(args))

fun(a=1,b=2,c=3)