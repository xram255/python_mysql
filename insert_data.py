import mysql.connector as conn

ppldb = conn.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)

cur = ppldb.cursor()
sql = "INSERT INTO people (name) VALUE ('Harry')"
cur.execute(sql)

ppldb.commit()

print('recode inserted..') 