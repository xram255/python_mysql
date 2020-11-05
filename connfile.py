import mysql.connector as mycon

try:
    conn = mycon.connect(host="145.14.144.145", user="root", passwd="FSGTcQT4kD39_5u")
    cur = conn.cursor()
    cur.execute("SHOW DATABASES")

    for x in cur:
        print(x)
except Exception as err:
    print (err)


