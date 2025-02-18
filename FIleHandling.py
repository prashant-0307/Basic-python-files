
def Details():
    firstname = input("Enter Name :")
    rollno = int(input("Enter Rollno"))

    print("Name :",firstname)
    print("Rollno :",rollno)


try:
    Details()
except:
    print("enter correct details")
