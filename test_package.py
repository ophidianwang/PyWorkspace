from od_package.od_module01 import od_class01

test_list = ['1','3838','ophidian']

oTest = od_class01.oInstanceByClass("ophidian")
oTest.go()

"""#class_foo("try class method: class_foo")	#wrong syntax
oTest.class_foo("try class method: oTest.class_foo")
od_class01.class_foo("try class method: od_class01.class_foo")

print "=========="

#static_foo("try static method: static_foo")	#wrong syntax
oTest.static_foo("try static method: oTest.static_foo")
od_class01.static_foo("try static method: od_class01.static_foo")"""

# import only module
from od_package import od_module_misc
od_module_misc.od_class_misc.html_dump(oTest)	# must call from module
od_module_misc.module_print("testing module_print")

print "=========="

# import class directly
from od_package.od_module_misc import od_class_misc
od_class_misc.html_dump(oTest)	# may call from class
od_class_misc.html_dump(test_list)

print "=========="

# import function directly
from od_package.od_module_misc import module_print
module_print("testing module_print (directly)")

print "=========="

from od_package.od_module_misc import od_class_go
#od_class_go.go("iwant-in")	#duplicate name (class and function)
od_class_go("is this ambigious?")