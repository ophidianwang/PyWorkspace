from pWebSite.mMisc import cUtf8Printer

dTest = {}
for x in xrange(1,10):	
	dTest["key"+str(x)] = "value'"+str(x)

cUtf8Printer().pprint(dTest)

sField = "(`" + "`,`".join(dTest.keys()) + "`)"
sValue = "(" + ",".join(["%s"]*len(dTest)) + ")"
sSql = "INSERT INTO " + sTable + " " + sField + " VALUES " + sValue

cUtf8Printer().pprint(sSql)