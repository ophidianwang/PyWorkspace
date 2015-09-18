#!/usr/bin/python

import numpy as np
import scipy as sp 
"""
a = np.arange(0,8).reshape(-1,4)
b = np.arange(1,5)
print( 'a' )
print( a )
print( 'b' )
print( b )
print('==========')
print( 'a + b' )
print( a + b )
print( 'a - b' )
print( a - b )
print( 'a * b' )
print( a * b )
print( 'a / b' )
print( a / b )
print( 'a // b' )
print( a // b )
print( '-a' )
print( -a )
print( 'a**b' )
print( a**b )
print( 'a % b' )
print( a % b )
"""

a = np.arange(12).reshape(2,3,2)
b = np.arange(12,24).reshape(2,2,3)
c = np.dot(a,b)

print(a)
print(b)
print(c)