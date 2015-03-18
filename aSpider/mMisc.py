# coding=utf8

import pprint	#module, not function
from datetime import datetime
from time import mktime
from time import strptime

class cUtf8Printer(pprint.PrettyPrinter):
	def format(self, object, context, maxlevels, level):
		if isinstance(object, unicode):
			return (object.encode('utf8'), True, False)
		return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)

def sDatetime(iTimestamp):
	return datetime.fromtimestamp(iTimestamp).strftime('%Y-%m-%d %H:%M:%S')

def iTimestamp(sDatetime):
	"input a datetime string, return timestamp"
	return int(mktime(strptime(sDatetime,'%Y-%m-%d %H:%M:%S')))

def vPrintR(mTarget,iLayer=0,sPreFix=""):
	"print an object's structure"
	iNextLayer = iLayer+1
	try:
		if type(mTarget) is str:
			print "\t"*iLayer + sPreFix + mTarget
		elif type(mTarget) is unicode:
			print "\t"*iLayer + sPreFix + mTarget.encode("utf-8")
		elif type(mTarget) is list:
			print "\t"*iLayer + sPreFix + "[" 
			for mAttr in mTarget:
				vPrintR(mAttr,iNextLayer)
			print "\t"*iLayer + "]" 
		elif type(mTarget) is tuple:
			print "\t"*iLayer + sPreFix + "(" 
			for mAttr in mTarget:
				vPrintR(mAttr,iNextLayer)
			print "\t"*iLayer + ")" 
		elif type(mTarget) is dict:
			print "\t"*iLayer + sPreFix + "{" 
			for sName in mTarget:
				vPrintR(mTarget[sName],iNextLayer,sName+":")
			print "\t"*iLayer + "}" 
		else:
			print "\t"*iLayer + sPreFix + str(mTarget)
	except:
		#supposed to be object?
		print "\t"*iLayer + sPreFix + "{" 
		lMember = [attr for attr in dir(mTarget) if not callable(getattr(mTarget,attr)) and not attr.startswith("__")]
		for sName in lMember:
			mAttr = getattr(mTarget,sName)
			vPrintR(mAttr,iNextLayer,sName+":")
		print "\t"*iLayer+"}"