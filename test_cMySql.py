from time import strftime
from pWebSite.mMySql import cMySql
from pWebSite.mMisc import cUtf8Printer

"""
oShell = cMySql.oDB("beauty2")

oCusor = oShell.oQuery("SELECT * FROM project LIMIT 0,10")

lData = cMySql.lFetchAll(oCusor)

for dSingle in lData:
	cUtf8Printer().pprint(dSingle)
"""

oShell = cMySql.oDB("test")

dInsert = {
	"content":"saodijt9pae8j b093582",
	"datetime":strftime('%Y-%m-%d %H:%M:%S')
}

cUtf8Printer().pprint(dInsert)

oShell.oInsert("test_py",dInsert)

oShell.vCommit()

cUtf8Printer().pprint("done")