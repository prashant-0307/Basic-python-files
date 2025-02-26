import mysql.connector as mycon

db = mycon.connect(host = "localhost" , user = "root" , password = "Prashant@123")

db_cursor = db.cursor()

update = "update mypython.demo set rollno = %s where name = %s"
set_val = (10 , "abc")

db_cursor.execute(update,set_val)
db.commit()
print("successfully updated")


db_cursor.execute("select * from mypython.demo")

for i in db_cursor.fetchall():
    print(i)