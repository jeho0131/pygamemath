from math import pi
from random import *

ci = 0
a = 0
x = random()
y = random()

for i in range(10000):
    if ((x*x)/4) + (y*y) < 1:
        ci += 1
    a += 1

    x = random()
    y = random()

print((pi * 2) / 4, ":", 2, " ≒ ", ci, ":", a)
print(((2*ci)/a)*4)
print("타원의 넓이 : ", pi*2)
