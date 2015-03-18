from datetime import datetime
from time import time
from time import gmtime
from time import mktime
from time import strptime

now = datetime.now()
utcnow = datetime.utcnow()
datetimeobj = datetime.fromtimestamp(time())


print now
print mktime(now.timetuple())
print time()
print utcnow
print mktime(utcnow.timetuple())
print gmtime()



strform = datetimeobj.strftime('%Y-%m-%d %H:%M:%S')
print strform

intform = int(mktime(strptime(strform,'%Y-%m-%d %H:%M:%S')))
print intform



