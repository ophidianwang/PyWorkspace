import numpy as np

def func2(i, j):
    return (i+1) * (j+1)
a = np.fromfunction(func2, (7,9))
print(a)

def word_set(M_max, N_max):
    word_list = []
    for M in xrange(M_max):
        for N in xrange(N_max):
            word_list.append( 'sim' + str(N) + "_word" + str(M) )
    return np.array(word_list).reshape(M_max,N_max)

arr = np.arange(12).reshape(-1,2)
print( arr +1 )
#print( word_set(3, 2) )

def func3(i,j):
    print( i )
    print( j )
    return i

arr2 = np.fromfunction( func2, (5,6) )

print( arr2 )

