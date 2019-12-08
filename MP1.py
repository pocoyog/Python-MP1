import matplotlib.pyplot as mpp
import math as mt
import numpy as np

print('         Machine Problem 1 (Python):          ')
print('This is a program in which implements a piecewise function to solve for f(n)')
print('from n = 0 to n = 99 by graphing using stem()')
print('The graph f(n) is shown below:')

y = list(np.zeros(100))
n = np.linspace(0,99,100)
for i in range(0,100,1):
    x = n[i]
    while x > 10 or x == 10:
        x = x - 10
    y[i] = x**2 - 7
    
    
    mpp.stem(n,y, use_line_collection = True)

mpp.xlabel('x-axis')
mpp.ylabel('y-axis')
mpp.grid(color='k', linestyle='-', linewidth=0.5)
