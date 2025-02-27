import mysql.connector as mycon

db = mycon.connect(host = "localhost" , user = "root" , password = "Prashant@123")
db_cursor = db.cursor() 

delete_q = "delete from mypython.demo where name = %s"
select_q = "select * from mypython.demo"
val_d = ("abc",)

insert_q = "insert into mypython.demo (name , rollno) values (%s , %s)"
val_i = ("abc" , 10)

try:
    db_cursor.execute(delete_q , val_d)   
    db.commit()
    print("deleted successfullly")
except:
    print("select correct records")

db_cursor.execute(select_q)
for i in db_cursor.fetchall():
    print(i)
print("data is empty")