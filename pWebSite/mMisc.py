# coding=utf8

import pprint	#module, not function

class cUtf8Printer(pprint.PrettyPrinter):
	def format(self, object, context, maxlevels, level):
		if isinstance(object, unicode):
			return (object.encode('utf8'), True, False)
		return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)

