import mysql.connector as mycon
from time import sleep as delay

conn = mycon.connect(host="localhost", user="root", password="", db="test")
cur = conn.cursor()
run_this = input("MySQL Command: ")
cur.execute(run_this)
for x  in cur:
    print(x)
    
cur.close()
conn.close()