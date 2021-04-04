import mysql.connector as mycon
conn = mycon.connect(host="localhost", user='root', passwd='', db='test')
cur = conn.cursor()

cur.execute("SELECT * FROM people WHERE name = 'Sara'")

results = cur.fetchall()

for x in results:
    print(x)

cur.close()
conn.close()

