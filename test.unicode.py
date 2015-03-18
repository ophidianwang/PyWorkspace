# coding=utf8
sContent = "\\'this is a content\\'"
sTest = "test a \'" + sContent + "\' "

origin = '這是中文'
uni = u'這是中文'

print "===================="
print origin
print type(origin)
print "===================="
print uni
print type(uni)
print "===================="

try:
	print "origin encode success: " + origin.encode('utf-8')
	print type(origin.encode('utf-8'))
except:
	print "origin encode failed"

print "===================="

try:
	print "uni encode success: " + uni.encode('utf-8')
	print type(uni.encode('utf-8'))
except:
	print "uni encode failed"

print "===================="

try:
	print "origin decode success: " + origin.decode('utf-8')
	print type(origin.decode('utf-8'))
except:
	print "origin decode failed"

print "===================="

try:
	print "uni decode success: " + uni.decode('utf-8')
	print type(uni.decode('utf-8'))
except:
	print "uni decode failed"

print "===================="

try:
	print "origin encode then decode success: " + origin.encode('utf-8').decode('utf-8')
	print type(origin.encode('utf-8').decode('utf-8'))
except:
	print "origin encode then decode failed"

print "===================="

try:
	print "uni encode then decode success: " + uni.encode('utf-8').decode('utf-8')
	print type(uni.encode('utf-8').decode('utf-8'))
except:
	print "uni encode then decode failed"	

print "===================="