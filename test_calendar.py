#!/usr/bin/python
try:
	import calendar
except ImportError:
	print "import falied"

cal = calendar.month(2008,1)
print "Here is the calendar:"
print cal;