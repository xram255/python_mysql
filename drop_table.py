import mysql.connector as mycon
#from time import sleep as delay

conn = mycon.connect(host="localhost", user="root", password="", db="test")
cur = conn.cursor()

try:
    cur.execute("DROP DATABASE test2")
except Exception as err:
    print(err, "\n", "closing")
    exit()


cur.execute("SHOW DATABASES")
for x in cur:
    print(x)

cur.close()
conn.close()