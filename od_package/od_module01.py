# encoding: utf-8

class od_class01:
	"""Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
        name: name of instance
    """
	count = 0
 
	def __init__(self, name):
		"""Inits SampleClass with blah."""
		self.name = name
		od_class01.count += 1
	 
	def __str__(self):
		return str(self.name)
		  
	def go(self):
		"test, print go! and self.__str__"
		print("go! " + self.__str__())
	 
	@classmethod
	def getX(cls):
		"get how many class instance is created"
		return cls.count

	@classmethod
	def class_foo(cls,x):
		"testing classmethod"
		print "executing class_foo(%s,%s)"%(cls,x)

	@staticmethod
	def static_foo(x):
		"testing staticmethod"
		print "executing static_foo(%s)"%x

	@classmethod
	def oInstanceByClass(cls,name):
		"testing get instance with classmethod"
		return od_class01(name)

	@staticmethod
	def oInstanceByStatic(name):
		"testing get instance with staticmethod"
		return od_class01(name)