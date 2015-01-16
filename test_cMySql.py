from pWebSite.mMySql import cMySql
from pWebSite.mMisc import cUtf8Printer

oShell = cMySql.oDB("beauty2")

oCusor = oShell.oQuery("SELECT * FROM project LIMIT 0,10")

lData = cMySql.lFetchAll(oCusor)

for dSingle in lData:
	cUtf8Printer().pprint(dSingle)

