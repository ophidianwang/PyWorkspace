# encoding: utf-8

import MySQLdb
from pprint import pprint

config = {
	"host":"172.16.2.41",
	"user":"robot",
	"passwd":"robot",
	"db":"galaxy_beauty2",
	"use_unicode":True
}

db = MySQLdb.connect(**config)
db.set_character_set("utf8")

cursor = db.cursor()

cursor.execute("SELECT * FROM project LIMIT 0,10")

data = cursor.fetchall()

#for single in data:
	#for val in single:
		#print val

#for field in cursor.description:
	#print field

pprint(data)
pprint(cursor.description)

db.close()