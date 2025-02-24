import mysql.connector as MC # type: ignore

obj = MC.connect(host = "localhost", user = "root" , password = "Prashant@123")
print(obj ,"connection successfully done")