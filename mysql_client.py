import mysql.connector as mycon

conn = mycon.connect(host="localhost", user="root", password="", db="corp")

cur = conn.cursor()

sql = '''INSERT INTO people (id, name, lastname, telephone, email, address)
VALUES (NULL, 'Anna', 'Williams', 899457, 'annawill@mail.com', '783/2, main st')
'''

try:
    cur.execute(sql)
    conn.commit()
    print("executed")
except Exception as err:
    conn.rollback()
    print(err, "\n", "closing..")
    exit()

cur.execute("SELECT * FROM people")

for x in cur:
    print(x)

cur.close()
conn.close()