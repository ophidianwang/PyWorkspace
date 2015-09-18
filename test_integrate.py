# -*- coding: utf-8 -*-

import numpy as np
from scipy import integrate

def half_circle(x):
    return (1-x**2)**0.5

N = 10000
x = np.linspace(-1, 1, N)
dx = 2.0/N
y = half_circle(x)

rect_sum = dx * np.sum(y[:-1] + y[1:]) # 面積的兩倍
print(rect_sum)

tzresult = np.trapz(y, x) * 2 # 面積的兩倍
print(tzresult)

pi_half, err = integrate.quad(half_circle, -1, 1)
quad_result = pi_half*2
print(quad_result)
