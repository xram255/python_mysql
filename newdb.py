import mysql.connector as mycon

conn = mycon.connect(host="145.14.144.145:3306", passwd="FSGTcQT4kD39_5u", user="id15090019_root", db="people")
cur = conn.cursor()
db_name = "acme"

def create_database(in_name):
    cur.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(in_name))
    print("Database {} Created ".format(in_name))
    
sql = '''INSERT INTO people(id, firstname, lastname, timestamp)
VALUES(NULL, 'Jason', 'Broody')
 '''

cur.execute(sql)
conn.commit()
cur.close()
conn.close()

#create_database("acme2")
