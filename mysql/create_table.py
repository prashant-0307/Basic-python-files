import mysql.connector as mycon

db = mycon.connect(host = "localhost" , user = "root" , password = "Prashant@123" , database = "mypython")

db_cursor = db.cursor()

try:
    db_cursor.execute("create table demo( name varchar(20), rollno int(5) )")
    print("table created......")
except:
    print("table already exists")