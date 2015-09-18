# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def func(x, p):
    """
    數據擬合所用的函數: A*sin(2*pi*k*x + theta)
    """
    A, k, theta = p
    return A*np.sin(2*np.pi*k*x+theta)   

def residuals(p, y, x):
    """
    實驗數據x, y和擬合函數之間的差，p為擬合需要找到的係數
    """
    return y - func(x, p)

x = np.linspace(0, -2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6 # 真實數據的函數參數
y0 = func(x, [A, k, theta]) # 真實數據
y1 = y0 + 2 * np.random.randn(len(x)) # 加入噪聲之後的實驗數據    

p0 = [7, 0.2, 0] # 第一次猜測的函數擬合參數

# 調用leastsq進行數據擬合
# residuals為計算誤差的函數
# p0為擬合參數的初始值
# args為需要擬合的實驗數據
plsq = leastsq(residuals, p0, args=(y1, x))

print u"真實參數:", [A, k, theta] 
print u"擬合參數", plsq[0] # 實驗數據擬合後的參數

pl.plot(x, y0, label=u"真實數據")
pl.plot(x, y1, label=u"帶噪聲的實驗數據")
pl.plot(x, func(x, plsq[0]), label=u"擬合數據")
pl.legend()
pl.show()