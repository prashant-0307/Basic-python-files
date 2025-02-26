import mysql.connector as mycon

db = mycon.connect(host = "localhost" , user = "root" , password = "Prashant@123" , database = "mypython")

db_cursor = db.cursor()

# single insert record 
# db_cursor.execute("insert into demo (name , rollno) values (%S,%s)",("asd" , 20))
# multiple record insert

db_insert = "insert into demo (name , rollno) values (%s , %s)"
db_val = [
    ("qwe",10),
    ("rty",20),
    ("uio",30)
]
db_cursor.executemany(db_insert,db_val)

db.commit()

print(db_cursor.rowcount,"was inserted")