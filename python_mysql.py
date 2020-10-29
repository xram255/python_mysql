import mysql.connector 

conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")

cur = conn.cursor()

db_names = ["test1", "test2", "test3"]
for db in db_names:
    cur.execute("CREATE DATABASE " + db)

cur.execute("SHOW DATABASES")
for x in cur:
    print(x)

cur.close()
conn.close()