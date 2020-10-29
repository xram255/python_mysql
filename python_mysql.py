import mysql.connector 

conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="")

cur = conn.cursor()

print(type(cur))
cur.execute("SHOW DATABASES")

for x in cur:
    print(x)

