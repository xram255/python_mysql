import mysql.connector as mycon
from time import sleep as delay

conn = mycon.connect(host="localhost", user="root", password="", db="test")
cur = conn.cursor()

while True:
    run_this = input("MySQL Command: ")

    if(run_this == "quit" or run_this == "QUIT"):
        break 

    try:
        cur.execute(run_this)
    except:
        conn.rollback()
    for x in cur:
        print(x)

cur.close()
conn.close()