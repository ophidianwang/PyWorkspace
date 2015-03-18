# encoding: utf-8
from time import strftime
from time import time
import datetime
from aSpider.pDatabase.mMySql import cMySql
from aSpider.mMisc import cUtf8Printer

import random
import string
from datetime import datetime


oDB = cMySql.oDB("test")


oCusor = oDB.oQuery("SELECT * FROM test LIMIT 0,10")

lData = cMySql.lFetchAll(oCusor)

for dSingle in lData:
	for key in dSingle:
		print type(dSingle[key])
	cUtf8Printer().pprint(dSingle)
	print dSingle

	uValue = dSingle['sValue']
	print uValue


"""
dInsert = {
	"content":"saodijt9pae8j b093582",
	"datetime":strftime('%Y-%m-%d %H:%M:%S')
}
"""
"""
sValue = "加進中文";
iCount = 0
while iCount<64:
	sValue += random.choice(string.ascii_letters)
	iCount+=1

dInsert = {
	"sValue":sValue,
	"iCreateTime":int(time())
}

cUtf8Printer().pprint(dInsert)

oDB.oInsert("test",dInsert)

oDB.vCommit()

cUtf8Printer().pprint("done")

dt = datetime.fromtimestamp(dInsert['iCreateTime'])

print dt
"""