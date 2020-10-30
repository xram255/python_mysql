import mysql.connector as mycon
from time import sleep as delay

conn = mycon.connect(host="localhost", user="root", password="", db="test")
cur = conn.cursor()

try:
    cur.execute("DROP DATABASE test2")
    delay(1)
    cur.execute("DROP DATABASE test3")
    delay(1)
except expression as identifier:
    print(identifier)
    


cur.execute("SHOW DATABASES")
for x in cur:
    print(x)


cur.close()
conn.close()