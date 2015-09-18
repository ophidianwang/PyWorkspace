import numpy as np

def func2(i, j):
    return (i+1) * (j+1)

a = np.fromfunction(func2, (9,9))

print(a)