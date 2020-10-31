import mysql.connector as mycon

conn = mycon.connect(host="localhost", user="root", password="", db="corp")

cur = conn.cursor()

sql = '''CREATE TABLE people
(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
telephone INT,
email VARCHAR(255),
address VARCHAR(100)
)'''

try:
    cur.execute(sql)
except Exception as exp:
    print("not executed", "\n", exp)
    conn.rollback()

for x in cur:
    print(x)

cur.close()
conn.close()