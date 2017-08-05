import MySQLdb
import config

conn = MySQLdb.connect("localhost", config.USERNAME, config.PASSWORD, "computerphile")   # host, uname, pw, dbname
C = conn.cursor()

C.execute("SELECT id, title from videos")
rows = C.fetchall()
print('testing')
for row in rows:
	print row[0], row[1]

modify = int(raw_input("Which video would you like to annotate? (Enter the id number)"))
note = raw_input("Note: ")

C.execute("SELECT count(*) from notes where video_id = %s" % modify)
count = C.fetchone()[0]

if count > 0:

	note = ' ' + note
	C.execute("Update notes set note = concat(note, '%s') where video_id = %s" % (note, modify) )
	conn.commit()

else:
	C.execute("INSERT INTO notes (note, video_id) VALUES ('%s', '%s')" % (note, modify))
	conn.commit()