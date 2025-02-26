import mysql.connector as mycon

db = mycon.connect(host = "localhost" , user = "root" , password = "Prashant@123" , database = "mypython")

db_cursor = db.cursor()

db_cursor.execute("select * from demo")

for i in db_cursor.fetchall():
    print(i)
