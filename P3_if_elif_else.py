
# conditional statement

# if 

# age = int(input("Enter your age for voting :"))

# if age >= 18 :
#     print("your are eligible for vote")
# else:
#     print("your not eligible for vote")


# elif
print("find larger number, enter 3 number :")
no_1 = int(input("enter 1 number :"))
no_2 = int(input("enter 2 number :"))
no_3 = int(input("enter 3 number :"))

if no_1 < no_2:
    print("larger number",no_1)
elif no_1 < no_3:
    print("larger number ",no_3)
else :
    print("larger number ",no_2)