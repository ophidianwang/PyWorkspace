from pprint import pprint

class od_class_misc(object):
	"""Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

	@staticmethod
	def html_dump(obj):
		print "<pre>"
		pprint(obj)
		print "</pre>"
		return

class od_class_go(object):

	@staticmethod
	def go(name):
		print "go go !"+name
		return

def module_print(message):

	#detect message's type
	msg_type = ''
	if type(message) is list:
		msg_type = 'list'
	elif type(message) is dict:
		msg_type = 'dict'
	elif type(message) is str:
		msg_type = 'str'
	elif type(message) is int:
		msg_type = 'int'
	else:
		msg_type = 'something else'

	print "module_print"
	print message
	return

def od_class_go(message):	#if module function and module class has same name, module function is called first
	print "od_module_misc.od_class_go:"+message
	return

