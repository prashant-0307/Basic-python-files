import mysql.connector as mycon

db = mycon.connect(host = "localhost" , user = "root" , password = "Prashant@123")

db_cursor = db.cursor()

db_cursor.execute("show databases")

for i in db_cursor:
    print(i)