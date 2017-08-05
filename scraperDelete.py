import MySQLdb
import config

conn = MySQLdb.connect("localhost", config.USERNAME, config.PASSWORD, "computerphile")   # host, uname, pw, dbname
C = conn.cursor()

C.execute("SELECT id, title from videos order by id asc")
rows = C.fetchall()

for row in rows:
    print row[0], row[1]

delete = int(raw_input("Enter the number of the video you would like to delete: "))

C.execute("SELECT title from videos where id = %s" % delete)
title = C.fetchall()
C.execute("DELETE FROM videos where id = %s" % delete)
conn.commit()
print "Sucessfully deleted %s" % title