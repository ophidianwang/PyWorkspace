import time

def my_print(var):
	"my_print document"
	print "OD's print:",var
	return

def my_datetime(timestamp):
	"my_datetime document"
	return time.localtime(timestamp)

def test_ref(count):
	print "in function before++:",count
	count = count+count
	print "in function after++:",count
	return

def test_ref2(list1):
	#list.append("appened")
	list2 = ["rewrite"]

	list1.extend(list2)
	print list1
	return