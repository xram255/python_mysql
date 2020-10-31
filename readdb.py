from mysql import connector as mycon

conn = mycon.connect(host="localhost", user="root", passwd="", db="corp")
cur = conn.cursor()

cmmnd = "SELECT email FROM people"

try:
    cur.execute(cmmnd)
    for x in cur:
        print(x)
except Exception as err:
    conn.rollback()
    cur.close()
    conn.close()
    print("not executed..! \n", err, "\n", "closing..")

cur.close()
conn.close()

