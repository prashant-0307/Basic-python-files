import mysql.connector as mycon # type: ignore 

db = mycon.connect(host = "localhost" , user = "root" , password = "Prashant@123")
db_cursor = db.cursor()
try:
    db_cursor.execute("create database mypython")
    print("database created successfully..........")
except:
    print("database already exists")