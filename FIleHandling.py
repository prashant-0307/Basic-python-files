
global a

def Details():
    global a
    firstname = input("Enter Name :")
    rollno = int(input("Enter Rollno"))
    a = int(input("enter std :"))

    print("Name :",firstname)
    print("Rollno :",rollno)

def show():
    print("intger :",a)


try:
    Details()
except:
    print("enter correct details")

show()