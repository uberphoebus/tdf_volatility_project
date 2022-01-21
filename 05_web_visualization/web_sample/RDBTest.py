#module name : RDBTest.py

import sqlite3

conn = sqlite3.connect("mydb.db")
cur = conn.cursor()
cur.execute("select * from user where id=? or pw=?", ['kim', 22,])
rows = cur.fetchall()  #rs.next()
for row in rows:
    print(row)
conn.close()




